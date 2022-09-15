import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    user_table = dynamodb.Table("user_table")
    username = event['username']
    
    try:
        response = user_table.get_item(
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