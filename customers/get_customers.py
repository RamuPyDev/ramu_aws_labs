import json
import boto3
import logging

import math 
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Customers')  # Update if your table name is different

def lambda_handler(event, context):
    try:
        
        logger.info(event)
        logger.info(context)
        userid = event['queryStringParameters']['id']

        logger.info(f"user id : {userid}")
        response = table.get_item(Key={'userid': userid})

        logger.info(f"Response: {response}")
        
        if 'Item' in response:
            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps(response['Item'])
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'User not found'})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
