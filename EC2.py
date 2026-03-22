import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    ImageId='ami-0abcdef12345',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='my-key'
)

print("EC2 created:", instance[0].id)
