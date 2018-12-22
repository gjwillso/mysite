import os
import boto3
import base64
import json
from botocore.exceptions import ClientError

#def get_secret():

secret_name = "DJANGO_SECRET_KEY"
region_name = "eu-west-1"

session = boto3.session.Session()
client = session.client(
    service_name='secretsmanager',
    region_name=region_name
)

try:
    get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        
except ClientError as e:
    if e.response['Error']['Code'] == 'DecryptionFailureException':
        raise e
    elif e.response['Error']['Code'] == 'InternalServiceErrorException':
        raise e
    elif e.response['Error']['Code'] == 'InvalidParameterException':
        raise e
    elif e.response['Error']['Code'] == 'InvalidRequestException':
        raise e
    elif e.response['Error']['Code'] == 'ResourceNotFoundException':
        raise e
else:
    if 'SecretString' in get_secret_value_response:
        secret = json.loads(get_secret_value_response['SecretString'])    
    else:
        decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])

print (secret['SECRET_KEY'])

