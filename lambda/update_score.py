import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    score_table = dynamodb.Table("score_table")
    username = event['username']
    word = event['word']
    score = int(event['score'])
    
    try:
        response = score_table.get_item(
            Key = {
                'username': username
            }    
        )['Item']
        
        top_score = 0
        if int(response['top_score']) > score:
            top_score = int(response['top_score'])
        else:
            top_score = score
        
        words_solved = response['words_solved']
        if word != '':
            words_solved.append(word)
            
        total_words_solved = len(words_solved)
    
        longest_word = max(words_solved, key=len)
        
        games_played = response['games_played'] + 1
        
        score_table.update_item(
            Key = {
                'username': username
            },
            UpdateExpression="set top_score=:s, total_words_solved=:n, words_solved=:w, longest_word_solved=:l, games_played=:g",
            ExpressionAttributeValues={
                ':s': top_score,
                ':n': total_words_solved,
                ':w': words_solved,
                ':l': longest_word,
                ':g': games_played
            }
        )
        
        return {
            'statusCode': 200,
            'body': {
                    'success': True,
                    'message': "Successfully updated score for user {}".format(username)
                }
        }
        
    except Exception as e:
        return {
            'statusCode': 400,
            'body': 'Error updating score for user {}. {}. 400'.format(username, e)
        }
        