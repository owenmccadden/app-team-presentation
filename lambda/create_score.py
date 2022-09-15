import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    score_table = dynamodb.Table("score_table")
    username = event['username']
    try:
        response = score_table.get_item(
            Key = {
                'username': username
            }    
        )
        
        if 'Item' in response:
            return {
                'statusCode': 200,
                'body': {
                    "success": False,
                    "message": "Failed to create score for user {}. User already exists.".format(username)
                }
            }
        else:
            score_table.put_item(
                Item={
                    "username": username,
                    "top_score": 0,
                    "total_words_solved": 0,
                    "words_solved": [],
                    "longest_word_solved": 0,
                    "games_played": 0
                }
            )
            return {
                'statusCode': 200,
                'body': {
                    'success': True,
                    "message": "Successfully created score for user {}".format(username)
                }
            }
    except Exception as e:
        return {
            "statusCode": 400,
            "body": "Error creating score for user {}. {}. 400".format(username, e)
        }
