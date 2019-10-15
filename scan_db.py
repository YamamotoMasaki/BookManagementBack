# -*- coding: utf-8 -*-

import json
import boto3
import re
import urllib

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('book-management-db')

def handler(event, context):
    
    # 送信先URL
    url = "https://master.dfxtb3bbf4p7x.amplifyapp.com/list/"
    
    #全件取得
    name = table.scan()
    
    # クエリ文字列の生成
    for i, item in enumerate(name["Items"]) :
        if i == 0 :
            url += "?{0}".format( urllib.parse.urlencode( item ) )
        else :
            url += "&{0}".format( urllib.parse.urlencode( item ) )
    
    #HTTPリダイレクトで返す
    return {"statusCode": 302,
            "headers": {"Location": url},
            "body": ""
    }
