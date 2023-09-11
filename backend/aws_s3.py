import boto3
import os
from dotenv import load_dotenv

load_dotenv()

access_key=os.environ["aws_access_key"]
secret_key=os.environ["aws_secret_key"]
s3 = boto3.client("s3", aws_access_key_id=f"{access_key}", aws_secret_access_key=f"{secret_key}", region_name="ap-south-1")