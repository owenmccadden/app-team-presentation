import json
import boto3
import urllib3

def lambda_handler(event, context):
    try:
        http = urllib3.PoolManager()
        response = http.request('GET', "https://random-word-api.herokuapp.com/word?number=1")
        word = response.data.decode("utf-8").split('"')[1]
        
        return {
            'statusCode': 200,
            'body': {
                "success": True,
                "message": "Successfully generated random word",
                "word": word
            }
        }
    except Exception as e:
        return {
            "statusCode": 400,
            "body": "Error generating word. {} 400".format(e)
        }