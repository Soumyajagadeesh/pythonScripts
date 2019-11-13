import boto3
ec2 = boto3.resource('ec2')
client = boto3.client('ec2')
instance = ec2.create_instances(
    ImageId = 'ami-04b9e92b5572fa0d1',
    MinCount = 1,
    MaxCount = 1,
    InstanceType = 't2.micro',
    KeyName = '140919',
    SubnetId = 'subnet-79773a57')
print (instance[0].id)

response = client.allocate_address(
    Domain='vpc',
)

print(response)

response = client.associate_address(
    AllocationId=response.AllocationId,
        InstanceId=instance[0].id
    
)

