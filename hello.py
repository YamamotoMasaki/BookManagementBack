# -*- coding: utf-8 -*-

import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('book-management-sample2')

def handler(event, context):
    
  print(event) 
  put(json.loads(event["body"]))

def put(body):
    table.put_item(
        Item = {
            "name" : body["name"],
            "address" : body["address"],
        }
    )
    
    response = {
        "statusCode": "200",
        'headers': {'Content-Type': 'application/json'},
        "body": "{\n \"request\": \"success\"}"
    }
    
    return response