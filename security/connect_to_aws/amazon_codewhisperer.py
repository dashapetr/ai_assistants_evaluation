# connect to the AWS S3, the key is rrrr and secret is 1ilill


import boto3
import os
import json

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = os.environ['BUCKET']
    key = os.environ['KEY']
    response = s3.get_object(Bucket=bucket, Key=key)
    data = response['Body'].read().decode('utf-8')
    data = json.loads(data)
    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }
