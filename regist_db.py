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
    
    # bodyは"bookname=xxx"の形式
    # 正規表現で分解
    #name = re.search(r"(?<=bookname=)(.*)", event["body"]).group()
    
    #bodyではなくqueryStringParametersに入ってるぽいのでお試し
    name = event["queryStringParameters"]
    
    # DBに挿入
    put(name["bookname"])
    
    # getパラメータ
    # param = [
    #     ( "bookname", name),
    # ]
    
    # クエリ文字列の生成
    url += "?{0}".format( urllib.parse.urlencode( name ) )
    
    print(url)
    
    return {"statusCode": 302,
            "headers": {"Location": url},
            "body": ""
    }
    
    # return {"statusCode": 200,
    #         "headers": {"Content-Type": "text/javascript"},
    #         "body": url
    # }

def put(body):
    
    table.put_item(
        Item = {
            "bookname" : body,
        }
    )
