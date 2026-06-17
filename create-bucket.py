import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3', region_name='ap-south-1')

bucket_name = 'kartik-bucket-987654321'

try:
    s3.head_bucket(Bucket=bucket_name)
    print("Bucket already exists!")
except ClientError:
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'ap-south-1'
        }
    )
    print("Bucket created successfully!")