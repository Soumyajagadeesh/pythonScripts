import boto3

client = boto3.client('iam')
response = client.add_user_to_group(
    GroupName='Docker',
    UserName='swathigoudar14'
)