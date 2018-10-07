import boto3
import os


# compare vpc.log with new_vpc.log
with open("new_vpc.log", 'r', encoding="utf=8") as new_vpc_log:
    new_line = new_vpc_log.readlines()
    new_line  # 새로운 log

with open("old_vpc.log", 'r', encoding="utf-8") as old_vpc_log:
    old_line = old_vpc_log.readlines()
    old_line  # 기존의 log(bucket에서 다운받은)


with open("old_vpc.log", 'a', encoding='utf-8') as f:
    for i in new_line:
        if i not in old_line:
            f.write(i)


# Create an S3 client
s3 = boto3.client('s3')

bucket_name = 'bigdata-msk'
# path = "C:/workspace/big_data/big-data-101/code/1_aws_cli_basics/log"
files = os.listdir('./')
# log_file = os.listdir()
if 'old_vpc.log' in files:
    filename = 'old_vpc.log'
    # for filename in files:
    s3.upload_file(filename, bucket_name, filename)
