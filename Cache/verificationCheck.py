#EMAIL VERIFICATION
from itertools import islice
import getpass
import boto3
from botocore.client import Config
from tkinter import messagebox


def verificationCheck(username, code):


    client = boto3.client(
        'cognito-idp',
        aws_access_key_id='',
        aws_secret_access_key='',
        config=Config(signature_version='s3v4')
    )
    try:



        response = client.confirm_sign_up(
            ClientId='',
            Username=username,
            ConfirmationCode=code,
            ForceAliasCreation=True,
            AnalyticsMetadata={
                'AnalyticsEndpointId': 'string'
            },
            UserContextData={
                'EncodedData': 'string'
            },
            ClientMetadata={
                'string': 'string'
            }
        )
        return True
    except:
        return False
