import boto3

s3 = boto3.client('s3', region_name="ap-southeast-1")
response = s3.list_buckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]

if 'bigdata-msk' not in buckets:
    response = s3.create_bucket(
        Bucket='bigdata-msk',
        CreateBucketConfiguration={
            'LocationConstraint': 'ap-southeast-1'
            }
        )
else:
    print('''bigdata-msk's name already exists''')
    
