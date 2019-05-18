"""
Common objects to maximize the benefit from AWS Lambda caching DynamoDB connections.
"""
import boto3


dynamodb_resource = boto3.resource('dynamodb', region_name='us-east-1')
ddb_table_word_dict = dynamodb_resource.Table('word_dictionary')
