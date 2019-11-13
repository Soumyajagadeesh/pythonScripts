import boto3
ec2 = boto3.resource('ec2')

response = client.allocate_address(
    Domain='standard'    
)
print(response)




