import boto3
import os
import json
from typing import Union


def get_s3_credentials(cred_file):
    with open(cred_file) as f:
        creds = json.load(f)
    return creds


def upload_to_s3(file_path, object_name=None):
    creds = get_s3_credentials("../../datalake-secret.json")
    bucket_name = creds["s3_bucket"]
    s3 = boto3.client(
        "s3",
        endpoint_url=creds["s3_endpoint"],
        aws_access_key_id=creds["s3_access_key_id"],
        aws_secret_access_key=creds["s3_secret_access_key"],
    )
    if object_name is None:
        object_name = file_path
    try:
        response = s3.upload_file(file_path, bucket_name, object_name)
    except Exception as e:
        print(e)
        return False
    return True


def upload_files_to_s3(file_list: Union[list, str]):
    # Iterate over files and upload each to the S3 bucket
    for file_path in file_list:
        upload_to_s3(file_path, os.path.join("WB", os.path.basename(file_path)))
