import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    score_table = dynamodb.Table('score_table')
    
    try:
        response = score_table.scan()
        sorted_items = sorted(response['Items'], key=lambda x: x['top_score'], reverse=True)
        return {
            'statusCode': 200,
            'body': sorted_items
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps('Error getting leaderboard. {} 400'.format(e))
        }