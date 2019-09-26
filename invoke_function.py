import boto3,argparse,json
from aws_provision import AwsClient
 
defaults = {"key" : None, "secret" : None}
parser = argparse.ArgumentParser()
parser.add_argument('-k',"--key")
parser.add_argument('-s',"--secret")
args = parser.parse_args()
    
command_line_args = {key:value for key,value in vars(args).items() if value}
key = command_line_args["key"]
secret = command_line_args["secret"]

#lambda_client = AwsClient('lambda',key,secret).client
#test_event = dict(plot_url="https://plot.ly/~chelsea_lyn/9008/")
# for i in range(1,100):
#     lambda_client.invoke(
#         FunctionName='myLambdaFunction',
#         InvocationType='Event',
#         Payload=json.dumps(test_event),
#     )
