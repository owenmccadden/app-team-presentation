import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    score_table = dynamodb.Table("score_table")
    username = event["username"]
    
    try:
        score_table.delete_item(
            Key={"username": username}
        )
        
        return {
            "statusCode": 200,
            "body": {
                "message": "Deleted score for user {}. 200".format(username),
                "success": True
            }
        }
    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps("Error deleting score for user {}. {}. 400".format(username, e))
        }