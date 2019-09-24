# Steps to use Boto3

## IAM Client

Create an IAM User and note down the User ARN which is a fully distinguished name for the user
User ARN sample: arn:aws:iam::{id}:user/{username}

Provide Administrator Access to this user or attach a specific role
Attach policies to the LambdaBasicExecution IAM Role (to enable writing into CloudWatch Logs)
 - AWSXrayWriteOnlyAccess
 - AwsLambdaBasicExecutionRole

# Lambda Client

Create a Lambda client with the zip file, and attach the role


`create_function(
            FunctionName='myLambdaFunction',
            Runtime='python3.6',
            Role=role['Role']['Arn'],
            Handler='main.handler',
            Code=dict(ZipFile=zipped_code),
            Timeout=300 # Maximum allowable timeout
        )`
