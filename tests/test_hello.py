# -*- coding: utf-8 -*-

import unittest
import hello

# Python のモックライブラリ
from moto import mock_dynamodb2, mock_dynamodb2_deprecated

import boto3
import json


class TestHandlerCase(unittest.TestCase):

    @mock_dynamodb2
    def test_response(self):
        
        # DynamoDBのモックの作成
        table_name = 'book-management-sample2'
        dynamodb = boto3.resource('dynamodb', 'ap-northeast-1')
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'name',
                    'KeyType': 'HASH'
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'name',
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
            "resource": "/lambdaproxy",
            "path": "/lambdaproxy",
            "httpMethod": "POST",
            "headers": {},
            "queryStringParameters": "",
            "pathParameters": "",
            "stageVariables": "",
            "requestContext": {},
            "body": "{\n \"name\": \"aaa\",\n\"address\": \"bbb\"\n}"
        }
        
        # 期待値の作成
        expected = [{
            "name": "aaa",
            "address": "bbb"
            }]
        
        # テスト対象を実行
        result = hello.handler(event, None)
        
        # 関数の呼び出し結果がテーブルから取り出した結果と一致するかを検証
        scan_result = table.scan()
        result_body = scan_result.get('Items')
        result_count = scan_result.get('Count')
        assert len(result_body) == result_count
        self.assertEqual(result_body, expected)
        

if __name__ == '__main__':
    unittest.main()
