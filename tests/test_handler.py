# -*- coding: utf-8 -*-

import unittest
import index
import botocore
import json

import os
# DynamoDBのモックで使われる、モックの環境変数
os.environ['TABLE_NAME'] = "book-management-sample2"
os.environ['KEY'] = "name"

## 設定に基づいて StringIO を取得
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
    
## Python のモックライブラリ
from mock import patch, call
from decimal import Decimal

@patch('botocore.client.BaseClient._make_api_call')
class TestHandlerCase(unittest.TestCase):

    def test_response(self, boto_mock):
        
        # DynamoDB テーブル内のモックの値
        items_in_db = [{'name': 'hoge', 'address': 'fuga'}
                    ]
        
        # DynamoDB テーブルのレスポンスのモック
        expected_ddb_response = {'Items': items_in_db}
        # boto を介して DynamoDB 呼び出すことによって返ってくることが期待されるレスポンスのモック
        response_body = botocore.response.StreamingBody(StringIO(str(expected_ddb_response)),
                                                        len(str(expected_ddb_response)))
        # モック内の期待される値をセット
        boto_mock.side_effect = [expected_ddb_response]
        # 実行中に、これらのパラメータを使用して DynamoDB Scan 関数が呼び出されることが期待されます
        expected_calls = [call('GetItem', {'TableName': os.environ['TABLE_NAME'], 'Key': {os.environ['KEY']: 'hoge'}} )]
        
        # テスト対象の関数呼び出し
        print("testing response.")
        result = index.handler(None, None)
        print(result)
        
        assert result.get('headers').get('Content-Type') == 'application/json'
        assert result.get('statusCode') == 200
        
        # 関数の呼び出し結果がテーブルから取り出した結果と一致するかを検証
        result_body = json.loads(result.get('body'))
        print(result_body.get('Items'))
        assert len(result_body) == len(items_in_db)
        self.assertEqual(result_body.get("Items")[0].get("name"), items_in_db[0].get("name")) # 雑
        
        assert boto_mock.call_count == 1
        boto_mock.assert_has_calls(expected_calls)

if __name__ == '__main__':
    unittest.main()
