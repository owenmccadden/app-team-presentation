import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    score_table = dynamodb.Table("score_table")
    username = event['username']
    
    try:
        response = score_table.get_item(
            Key={
                "username": username
            }  
        )
        return {
            "statusCode": 200,
            "body": response
        }
        
    except Exception as e:
        return {
            'statusCode': 400,
            'body': 'Error getting user {}. {} 400'.format(username, e)
        }