import json
import boto3
import hashlib

def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    user_table = dynamodb.Table("user_table")
    username = event['username']
    password = hashlib.sha512(str.encode(event['password'])).hexdigest()
    new_password = hashlib.sha512(str.encode(event['new_password'])).hexdigest()
    passwords_match = False
    
    try:
        response = user_table.get_item(
            Key={
                "username": username
            }    
        )

        old_password = response['Item']['password']
        
        if old_password == password:
            passwords_match = True
            user_table.update_item(
                Key={
                    'username': username
                },
                UpdateExpression="set password=:p",
                ExpressionAttributeValues={
                    ':p': new_password
                }
            )
            return {
            'statusCode': 200,
            'body': {
                "message": "Passwords match. Successfully updated password for user {}".format(username),
                "success": passwords_match
                }
            }
        else:
            return {
            'statusCode': 200,
            'body': {
                "message": "Passwords do not match. Failed to update password for user {}".format(username),
                "success": passwords_match
                }
            }
    except Exception as e:
        return {
            "statusCode": 400,
            "body": "Error updating password for user {}. {}. 400".format(username, e)
        }