import json, boto3
import argparse
import os
from collections import ChainMap

class AwsClient:
    def __init__(self,client_name,key,secret):
        if client_name is 'lambda':
            region_name='us-west-2'
            self.client = boto3.client(client_name,aws_access_key_id=key,aws_secret_access_key=secret,region_name=region_name)
        else:
            self.client = boto3.client(client_name,aws_access_key_id=key,aws_secret_access_key=secret)


def main():
    # Can provide AWS access key in 3 ways: init , environment var and defaults
    defaults = {"key" : None, "secret" : None}
    parser = argparse.ArgumentParser()
    parser.add_argument('-k',"--key")
    parser.add_argument('-s',"--secret")
    args = parser.parse_args()
    
    # chain map the command line args
    command_line_args = {key:value for key,value in vars(args).items() if value}
    chain =  ChainMap(command_line_args,os.environ, defaults)
    if chain["key"] == None:
        print("No AWS key/secret found")
    else:
        return chain["key"],chain["secret"]
        
    #lambda_client = boto3.client('lambda')
    #with open('lambda.zip','rb') as f:
     #   archive = f.read()

def init_lambda_execution_policy(iam_client,key, secret):
    role_policy_document = {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Sid": "",
               "Effect": "Allow",
               "Principal": {
                 "Service": "lambda.amazonaws.com"
               },
               "Action": "sts:AssumeRole"
             }
           ]
        }
    iam_client.create_role(
     RoleName='LambdaBasicExecution',
        AssumeRolePolicyDocument=json.dumps(role_policy_document),
    )
    iam_client.create_role(
        RoleName='AWSLambdaBasicExecutionRole',
        AssumeRolePolicyDocument=json.dumps(role_policy_document)
    )
    print(iam_client.get_role(RoleName='AWSLambdaBasicExecutionRole'))

if __name__ == "__main__":
    key,secret = main()
    if key is not None and secret is not None:
        iam_client = AwsClient('iam',key,secret).client
        #init_lambda_execution_policy(iam_client,key,secret)
        lambda_client = AwsClient('lambda',key,secret).client
        with open('lambda.zip', 'rb') as f:
            zipped_code = f.read()
        role = iam_client.get_role(RoleName='LambdaBasicExecution')
        lambda_client.create_function(
            FunctionName='myLambdaFunction',
            Runtime='python3.6',
            Role=role['Role']['Arn'],
            Handler='main.handler',
            Code=dict(ZipFile=zipped_code),
            Timeout=300 # Maximum allowable timeout
        )



