# -*- coding: utf-8 -*-

import json
import boto3
import re
import urllib

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('book-management-db')

def handler(event, context):
    
    # 送信先URL
    url = "https://master.dfxtb3bbf4p7x.amplifyapp.com/registResult"
    
    # 正規表現で分解
    name = re.search(r"(?<=bookname=)(.*)", event["body"]).group()
    
    # DBに挿入
    put(name)
    
    # getパラメータ
    param = [
        ( "bookname", name),
    ]
    
    # クエリ文字列の生成
    url += "?{0}".format( urllib.parse.urlencode( param ) )

    
    return {'statusCode': 201,
            'headers': {'Location': url}}

# bodyは"name=xxx"の形式
def put(body):
    
    table.put_item(
        Item = {
            "bookname" : body,
        }
    )
