import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    user_table = dynamodb.Table("user_table")
    username = event['username']
    new_email = event['email']
    
    try:
        user_table.update_item(
                Key={
                    'username': username
                },
                UpdateExpression="set email=:e",
                ExpressionAttributeValues={
                    ':e': new_email
                }
            )
            
        return {
            'statusCode': 200,
            'body': {
                "message": "Updated email for user {}. 200".format(username),
                "success": True
            }
        }
    except Exception as e:
        return {
            "statusCode": 400,
            "body": "Error updating email for user {}. {}. 400".format(username, e)
        }