import boto3

ec2 = boto3.resource(
    'ec2',
    region_name='ap-south-1'
)

instances = ec2.create_instances(
    ImageId='ami-0f58b397bc5c1f2e8',
    MinCount=1,
    MaxCount=1,
    InstanceType='t3.micro'
)

print("Instance ID:", instances[0].id)