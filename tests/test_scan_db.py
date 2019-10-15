# -*- coding: utf-8 -*-

import unittest
import scan_db

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
        
        #テストデータの作成
        table.put_item(
            Item = {
                'bookname' : 'aaa',
            }
        )
        
        table.put_item(
            Item = {
                'bookname' : 'bbb',
            }
        )
        
        table.put_item(
            Item = {
                'bookname' : 'ccc',
            }
        )
        
        # 期待値の作成
        expected = {'statusCode': 302, 
                    'headers': {'Location': 'https://master.dfxtb3bbf4p7x.amplifyapp.com/list/?bookname=aaa&bookname=bbb&bookname=ccc'}, 
                    'body': ''}
        
        # テスト対象を実行
        result = scan_db.handler(None, None)
        
        # 関数の呼び出し結果検証
        self.assertEqual(expected, result)
        

if __name__ == '__main__':
    unittest.main()
