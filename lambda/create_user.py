import json
import boto3
import hashlib

def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb')
    user_table = dynamodb.Table('user_table')
    username = event['username']
    
    try:
        response = user_table.get_item(
            Key = {
                'username': event['username']
            }    
        )
        
        if 'Item' in response:
            return {
                'statusCode': 200,
                'body': {
                    "success": False,
                    "message": "User {} already exists. Failed to create user.".format(username)
                }
            }
        else :
            user_table.put_item(
                Item = {
                    'username': username,
                    'password': hashlib.sha512(str.encode(event['password'])).hexdigest(),
                    'email': event['email']
                } 
            )
        
            return {
                'statusCode': 200,
                'body': {
                    "success": True,
                    "message": "Successfully created user {}".format(username),
                    "username": username
                }
            }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': "Error creating the user {}. {}. {}. 400".format(username, e, response)
        }