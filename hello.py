# -*- coding: utf-8 -*-

import json
import boto3
import re

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('book-management-sample2')

def handler(event, context):
  print(event["body"])
  put(event["body"])

# bodyは"name=xxx&address=xxx"の形式
def put(body):
    
    # 本当はurllibのparseを使いたかったが、なぜかできなかったので、正規表現で分解
    name = re.search(r"(?<=name=)(.*)(?=&)", body).group()
    print(name)
    address = re.search(r"(?<=&address=)(.*)", body).group()
    
    table.put_item(
        Item = {
            "name" : name,
            "address" : address,
        }
    )
    
    response = {
        "statusCode": "200",
        'headers': {'Content-Type': 'application/json'},
        "body": "{\n \"request\": \"success\"}"
    }
    
    return response