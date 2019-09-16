# -*- coding: utf-8 -*-

import unittest
from src import regist_db

# Python のモックライブラリ
from moto import mock_dynamodb2

import boto3
import json


class TestHandlerCase(unittest.TestCase):

    @mock_dynamodb2
    def test_response(self):
        
        # DynamoDBのモックの作成
        table_name = 'book-management-db'
        
        #東京リージョン
        dynamodb = boto3.resource('dynamodb', 'ap-northeast-1')
        
        #オハイオリージョン
        #dynamodb = boto3.resource('dynamodb', 'us-east-2')
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'bookname',
                    'KeyType': 'HASH'
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'bookname',
                    'AttributeType': 'S'
                },

            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        
        # 入力値の作成
        event = {
            'path': '/regist_db',
            'httpMethod': 'POST', 
            'headers': {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'ja,en-US;q=0.9,en;q=0.8', 'cache-control': 'max-age=0', 'CloudFront-Forwarded-Proto': 'https', 'CloudFront-Is-Desktop-Viewer': 'true', 'CloudFront-Is-Mobile-Viewer': 'false', 'CloudFront-Is-SmartTV-Viewer': 'false', 'CloudFront-Is-Tablet-Viewer': 'false', 'CloudFront-Viewer-Country': 'JP', 'content-type': 'application/x-www-form-urlencoded', 'Host': 'in1r9v7w00.execute-api.ap-northeast-1.amazonaws.com', 'origin': 'https://87230f29850846c38335ec0e36f7c0e5.vfs.cloud9.ap-northeast-1.amazonaws.com', 'Referer': 'https://87230f29850846c38335ec0e36f7c0e5.vfs.cloud9.ap-northeast-1.amazonaws.com/lambda/', 'upgrade-insecure-requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36', 'Via': '2.0 b34fbbb86a3a9401c6bffb8bf0be4217.cloudfront.net (CloudFront)', 'X-Amz-Cf-Id': 'X9-UJccTpkDU8jfH4rfm7vWU2HQ_vrvWmxW5_QThD-XTro2nxLejhQ==', 'X-Amzn-Trace-Id': 'Root=1-5d466c89-ac4155c4a50e1e370daf58be', 'X-Forwarded-For': '118.236.183.189, 70.132.40.158', 'X-Forwarded-Port': '443', 'X-Forwarded-Proto': 'https'},
            'multiValueHeaders': {'Accept': ['text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'], 'Accept-Encoding': ['gzip, deflate'], 'Accept-Language': ['ja,en-US;q=0.9,en;q=0.8'], 'cache-control': ['max-age=0'], 'CloudFront-Forwarded-Proto': ['https'], 'CloudFront-Is-Desktop-Viewer': ['true'], 'CloudFront-Is-Mobile-Viewer': ['false'], 'CloudFront-Is-SmartTV-Viewer': ['false'], 'CloudFront-Is-Tablet-Viewer': ['false'], 'CloudFront-Viewer-Country': ['JP'], 'content-type': ['application/x-www-form-urlencoded'], 'Host': ['in1r9v7w00.execute-api.ap-northeast-1.amazonaws.com'], 'origin': ['https://87230f29850846c38335ec0e36f7c0e5.vfs.cloud9.ap-northeast-1.amazonaws.com'], 'Referer': ['https://87230f29850846c38335ec0e36f7c0e5.vfs.cloud9.ap-northeast-1.amazonaws.com/lambda/'], 'upgrade-insecure-requests': ['1'], 'User-Agent': ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'], 'Via': ['2.0 b34fbbb86a3a9401c6bffb8bf0be4217.cloudfront.net (CloudFront)'], 'X-Amz-Cf-Id': ['X9-UJccTpkDU8jfH4rfm7vWU2HQ_vrvWmxW5_QThD-XTro2nxLejhQ=='], 'X-Amzn-Trace-Id': ['Root=1-5d466c89-ac4155c4a50e1e370daf58be'], 'X-Forwarded-For': ['118.236.183.189, 70.132.40.158'], 'X-Forwarded-Port': ['443'], 'X-Forwarded-Proto': ['https']},
            'queryStringParameters': None,
            'multiValueQueryStringParameters': None,
            'pathParameters': None,
            'stageVariables': None,
            'requestContext': {'resourceId': 'c6u4ev', 'resourcePath': '/regist_db', 'httpMethod': 'POST', 'extendedRequestId': 'd4XleG7YNjMFu7Q=', 'requestTime': '04/Aug/2019:05:26:33 +0000', 'path': '/Prod/regist_db', 'accountId': '478293598449', 'protocol': 'HTTP/1.1', 'stage': 'Prod', 'domainPrefix': 'in1r9v7w00', 'requestTimeEpoch': 1564896393435, 'requestId': '6bea2b26-b678-11e9-84d6-1f74cb645a4d', 'identity': {'cognitoIdentityPoolId': None, 'accountId': None, 'cognitoIdentityId': None, 'caller': None, 'sourceIp': '118.236.183.189', 'principalOrgId': None, 'accessKey': None, 'cognitoAuthenticationType': None, 'cognitoAuthenticationProvider': None, 'userArn': None, 'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36', 'user': None}, 'domainName': 'in1r9v7w00.execute-api.ap-northeast-1.amazonaws.com', 'apiId': 'in1r9v7w00'},
            'body': 'bookname=aaa',
            'isBase64Encoded': False
        }
        
        # 期待値の作成
        expected = [{
            "bookname": "aaa",
            }]
        
        # テスト対象を実行
        result = regist_db.handler(event, None)
        
        # 関数の呼び出し結果がテーブルから取り出した結果と一致するかを検証
        scan_result = table.scan()
        result_body = scan_result.get('Items')
        self.assertEqual(result_body, expected)
        

if __name__ == '__main__':
    unittest.main()
