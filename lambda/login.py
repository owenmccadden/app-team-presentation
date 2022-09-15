import json
import boto3
import hashlib

def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    user_table = dynamodb.Table("user_table")
    username = event['username']
    password = hashlib.sha512(str.encode(event['password'])).hexdigest()

    try:
        response = user_table.get_item(
            Key={
                "username": username
            }    
        )
   
        if 'Item' in response:
            stored_password = response['Item']['password']
            if stored_password == password:
                 return {
                     'statusCode': 200,
                     'body': {
                        "success": True,
                        "message": "Passwords match. Successfully logged in user {}".format(username),
                        "username": username
                     }
                 }
            
        return {
            'statusCode': 200,
            'body': {
                "success": False,
                "message": "Passwords do not match. Failed to log in user {}".format(username)
            }
        }
            
        
    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps("Error updating password for user {}. {}. 400".format(username, e))
        }