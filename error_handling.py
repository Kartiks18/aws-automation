import boto3
from botocore.exceptions import ClientError

try:
    s3 = boto3.client("s3")

    response = s3.list_buckets()

    print("Connected to AWS successfully!")

except ClientError as e:
    print("AWS Error:")
    print(e)