# -*- coding: utf-8 -*-

import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('book-management-sample2')

def handler(event, context):
  put(json.loads(event["body"]))

def put(body):
    result = table.put_item(
        Item = {
            "name" : body["name"],
            "address" : body["address"],
        }
    )
    return result