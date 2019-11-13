import boto3

s3 = boto3.resource('s3')
response = s3.create( Bucket="ankit202920291",ACL='public-read',CreateBucketConfiguration={'LocationConstraint': 'us-east-2' } )