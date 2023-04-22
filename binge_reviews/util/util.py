import os
import boto3
from botocore.exceptions import ClientError
from flask import request
from werkzeug.utils import secure_filename
from datetime import datetime


s3_bucket_name = "binge-reviews"
s3_bucket_url = "https://binge-reviews.s3.eu-north-1.amazonaws.com/"
client = boto3.client('s3',
                      aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
                      aws_secret_access_key=os.environ.get(
                          "AWS_SECRET_ACCESS_KEY"))


def upload_image(stored_file: str) -> str:
    """
    This function stores a file in an AWS S3 bucket using boto3
    The filename is the name of file added by the user
    When the file is successfully stored in the s3 bucket, then image_url is
    returned
    :param stored_file: Name of file to store in AWS S3 bucket
    :return image_url: Image url of image in AWS S3 bucket
    """
    image = request.files[stored_file]
    image_file = secure_filename(image.filename)
    image_to_upload = image_file
    try:
        s3 = boto3.resource('s3')
        s3.Bucket(s3_bucket_name).put_object(
            Key=image_to_upload, Body=image)
    except ClientError:
        raise Exception("Error when uploading image to S3 bucket")

    image_url = s3_bucket_url + image_to_upload
    return image_url


def get_timestamp() -> str:
    """
    This Function generates a timestamp.
    :return timestamp:
    """
    now = datetime.now()
    timestamp = now.strftime("%d %B, %Y")

    return timestamp
