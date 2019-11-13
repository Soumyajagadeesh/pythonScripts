import boto3
ec2 = boto3.resource('ec2')
s3 = boto3.resource('s3')
client = boto3.client('iam')

response = s3.create_bucket( Bucket="ankit20292029231",ACL='public-read')

instance = ec2.create_instances(
    ImageId = 'ami-04b9e92b5572fa0d1',
    MinCount = 1,
    MaxCount = 1,
    InstanceType = 't2.micro',
    KeyName = '140919',
    SubnetId = 'subnet-79773a57')
print (instance[0].id)

response = client.create_user(
    UserName='swathigoudar141',
    Tags=[
        {
            'Key': 'name',
            'Value': 'Swathi GR'
        },
    ]
)


response = client.add_user_to_group(
    GroupName='Docker',
    UserName='swathigoudar141',
)

print(response)


response = client.attach_user_policy(
    UserName='swathigoudar14',
    PolicyArn='arn:aws:iam::aws:policy/AmazonS3FullAccess'
)