import boto3
import botocore
import os

BUCKET_NAME = 'bigdata-msk' # replace with your bucket name
KEY = 'new_vpc.log' # replace with your object key

s3 = boto3.resource('s3')
# path_dir = 'C:/workspace/big_data/big-data-101/code/1_aws_cli_basics/vpc/log'
# file_list = os.listdir(path_dir)
# file_list
#
# if KEY in file_list:
#     with open("vpc.log", 'r', encoding="utf-8") as log_file:
#         log_line = log_file.readline()

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, 'old_vpc.log')

except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise
