import os
import boto
from botocore.exceptions import ClientError
from flask import request
from werkzeug.utils import secure_filename

# AWS S3 variables
s3_bucket_binge = "binge-reviews"
s3_bucket_url = "s3://arn:aws:s3:eu-north-1:562164357118:accesspoint/binge-reviews-imgs"
client = boto3.client('s3',
                      aws_access_key=os.environ.get("AWS_ACCESS_KEY"),
                      aws_secret_key=os.envron.get("AWS_SECRET_KEY"))


def generate_timestamp() -> str:
    """
    This function generates a timestamp
    :return timestamp: Unique timestamp
    """
    now = datetime.now()
    timestamp = now.strftime("%Y_%m_%d_%H_%M_%S_")
    return timestamp


def store_img_in_aws_bucket(file_to_store: str) -> str:
    """
    This function stores the file in a aws s3 bucket
    using boto3
    """
    image = request.files[file_to_store]
    image_file = secure_filename(image.filename)
    image_upload = timestamp + image_file
    try:
        s3 = boto3.resource('s3')
        s3.Bucket(s3_bucket_binge).put_object(Key=image_upload, Body=image)
    except ClientError:
        raise Exception("Exception when uploading the image to S3 bucket")

    image_url = s3_bucket_url + image_upload
    return image_url


def is_image_type_allowed(file_name: str) -> Tuple[str, Tuple[str]]:
    """
    This function takes a filename and returns the image type an
    allowed file types of jpg, JPG, png and PNG
    :param file_name: Name of file
    :return image_type, allowed_image_file_types: Image type and list
    of allowed file types
    """
    allowed_image_file_types = ["jpg", "JPG", "png", "PNG"]
    image = request.files[file_name]
    image_type = secure_filename(image.filename).rsplit('.', 1)[1]
    return image_type, allowed_image_file_types
