import os
import boto
from botocore.exceptions import ClientError
from flask import request
from werkzeug.utils import secure_filename

# AWS S3 variables
s3_bucket_name = "binge-reviews"
s3_bucket_url = "s3://arn:aws:s3:eu-north-1:562164357118:accesspoint/binge-reviews-imgs"
client = boto3.client('s3',
                      aws_access_key=os.environ.get("AWS_ACCESS_KEY"),
                      aws_secret_key=os.envron.get("AWS_SECRET_KEY"))
