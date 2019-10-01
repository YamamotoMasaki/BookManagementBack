# -*- coding: utf-8 -*-

import json
import boto3
import re
import urllib

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('book-management-db')

def handler(event, context):
    
    # 送信先URL
    url = "https://master.dfxtb3bbf4p7x.amplifyapp.com/registResult/"
    
    #bodyではなくqueryStringParametersに入ってる
    name = event["queryStringParameters"]
    
    # DBに挿入
    put(name["bookname"])
    
    # クエリ文字列の生成
    url += "?{0}".format( urllib.parse.urlencode( name ) )
    
    #HTTPリダイレクトで返す
    return {"statusCode": 302,
            "headers": {"Location": url},
            "body": ""
    }

def put(body):
    
    table.put_item(
        Item = {
            "bookname" : body,
        }
    )
