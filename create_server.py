import boto3
ec2 = boto3.resource('ec2', region_name="ap-southeast-1")

web_application = ec2.create_instances(
    NetworkInterfaces=[{'SubnetId': "subnet-538b8334", 'DeviceIndex': 0, 'Groups': ["sg-06f6a15c5a6cc32f4"]}],
    ImageId='ami-012023932de5a4632', # write Image_id
    MinCount=1,
    MaxCount=1,
    KeyName="IME_Bigdata",
    InstanceType="t2.micro"
    )

crontab_server = ec2.create_instances(
    NetworkInterfaces=[{'SubnetId': "subnet-538b8334", 'DeviceIndex': 0, 'Groups': ["sg-06f6a15c5a6cc32f4"]}],
    ImageId='ami-0fc710c6659aee053', # write Image_id
    MinCount=1,
    MaxCount=1,
    KeyName="IME_Bigdata",
    InstanceType="t2.micro"
    )
