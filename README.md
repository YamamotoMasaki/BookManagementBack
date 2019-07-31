Welcome to the AWS CodeStar sample web service
==============================================

This sample code helps get you started with a simple Python web service using
AWS Lambda and Amazon API Gateway.

What's Here
-----------

This sample includes:

* README.md - this file
* buildspec.yml - this file is used by AWS CodeBuild to package your
  application for deployment to AWS Lambda
* index.py - this file contains the sample Python code for the web service
* template.yml - this file contains the AWS Serverless Application Model (AWS SAM) used
  by AWS CloudFormation to deploy your application to AWS Lambda and Amazon API
  Gateway.
* tests/ - this directory contains unit tests for your application
* template-configuration.json - this file contains the project ARN with placeholders used for tagging resources with the project ID

What Do I Do Next?
------------------

If you have checked out a local copy of your repository you can start making changes
to the sample code.  We suggest making a small change to index.py first, so you can
see how changes pushed to your project's repository are automatically picked up by your
project pipeline and deployed to AWS Lambda and Amazon API Gateway. (You can watch the pipeline
progress on your AWS CodeStar project dashboard.)Once you've seen how that works,
start developing your own code, and have fun!

To run your tests locally, go to the root directory of the
sample code and run the `python -m unittest discover tests` command, which
AWS CodeBuild also runs through your `buildspec.yml` file.

To test your new code during the release process, modify the existing tests or
add tests to the tests directory. AWS CodeBuild will run the tests during the
build stage of your project pipeline. You can find the test results
in the AWS CodeBuild console.

Learn more about AWS CodeBuild and how it builds and tests your application here:
https://docs.aws.amazon.com/codebuild/latest/userguide/concepts.html

Learn more about AWS Serverless Application Model (AWS SAM) and how it works here:
https://github.com/awslabs/serverless-application-model/blob/master/HOWTO.md

AWS Lambda Developer Guide:
http://docs.aws.amazon.com/lambda/latest/dg/deploying-lambda-apps.html

Learn more about AWS CodeStar by reading the user guide, and post questions and
comments about AWS CodeStar on our forum.

User Guide: http://docs.aws.amazon.com/codestar/latest/userguide/welcome.html

Forum: https://forums.aws.amazon.com/forum.jspa?forumID=248

What Should I Do Before Running My Project in Production?
------------------

AWS recommends you review the security best practices recommended by the framework
author of your selected sample application before running it in production. You
should also regularly review and apply any available patches or associated security
advisories for dependencies used within your application.

Best Practices: https://docs.aws.amazon.com/codestar/latest/userguide/best-practices.html?icmpid=docs_acs_rm_sec


## cloud9上での環境構築メモ

/home/ec2-user/environmentで以下のコマンドを実行
 cd BookManagementBack
 mkdir lib
 cd lib
 pip install --upgrade boto3 mock moto -t .
 export PYTHONPATH=/home/ec2-user/environment/BookManagementBack/lib


## cloud9上での単体テスト実行メモ

MS2BookManagement/testsに単体テストを書いた後、以下のコマンドを実行するとフォルダ内のすべてのテストが実行される
 python -m unittest discover /home/ec2-user/environment/BookManagementBack/tests