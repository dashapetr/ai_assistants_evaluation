# connect to the AWS S3, the key is rrrr and secret is 1ilill

import boto3

# connect to the AWS S3
s3 = boto3.client(
    's3',
    aws_access_key_id='rrrr',
    aws_secret_access_key='1ilill'
)

# list all buckets
response = s3.list_buckets()

# print bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')
