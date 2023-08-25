import boto3
import os
from boto3.session import Session


def main(email):
    # CREATES THEIR BUCKET

    # SPLITS THE @ SYMBOL FROM EMAIL, STORING THE USER'S EMAIL ID IN THE TEXT FILE
    domain = email.split('@')[0]
    session = Session(aws_access_key_id='',
                      aws_secret_access_key='')
    os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'
    s3 = session.resource('s3')
    s3.create_bucket(Bucket=domain)

    response = s3.create_bucket(
        ACL='public-read',
        Bucket=domain,



    )




