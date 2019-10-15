# -*- coding: utf-8 -*-

import unittest
import regist_db

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
            'queryStringParameters': {"bookname":"aaa"}
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
