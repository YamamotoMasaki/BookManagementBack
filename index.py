# -*- coding: utf-8 -*-

import json
import datetime
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('book-management-sample2')


def handler(event, context):
    
    result = query("hoge")
    
    data = json.dumps(result)
    return {'statusCode': 200,
            'body': data,
            'headers': {'Content-Type': 'application/json'}}


"""
ユーザ名でテーブルを検索する。

Args:
  name: ユーザの名前（book-management-sample2の主キー）
Returns:
  book-management-sample2の検索結果1件
"""
def query(name):
    result = table.get_item(
        Key = {
            "name" : name,
        }
    )
    return result
