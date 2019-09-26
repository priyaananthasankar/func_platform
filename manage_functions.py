import boto3,argparse,json
from aws_provision import AwsClient

def delete(func_prefix,range_val):
    for i in range(1,range_val):
        func_name = func_prefix + str(i)
        response = lambda_client.delete_function(
            FunctionName=func_name
        )
        print(response)

if __name__ == "__main__":

    defaults = {"key" : None, "secret" : None}
    parser = argparse.ArgumentParser()
    parser.add_argument('-k',"--key")
    parser.add_argument('-s',"--secret")
    parser.add_argument('-d',"--delete")
    parser.add_argument('-r',"--range")
    args = parser.parse_args()
        
    command_line_args = {key:value for key,value in vars(args).items() if value}
    key = command_line_args["key"]
    secret = command_line_args["secret"]
    func_name = command_line_args["delete"]
    range_val = command_line_args["range"]

    lambda_client = AwsClient('lambda',key,secret).client
    delete(func_name,int(range_val))






