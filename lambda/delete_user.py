import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    user_table = dynamodb.Table("user_table")
    username = event["username"]
    try:
        user_table.delete_item(
            Key={"username": username}
        )
        
        return {
            "statusCode": 200,
            "body": {
                "message": "Deleted user {}. 200".format(username),
                "success": True
            }
        }
    except Exception as e:
        return {
            "statusCode": 400,
            "body": "Error deleting user {}. {}. 400".format(username, e)
        }