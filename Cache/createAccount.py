# CREATES THE ACCOUNT WITH COGNITO
from itertools import islice
import getpass
import boto3
from botocore.client import Config
from tkinter import messagebox


def createAccount(username, password):
    print(username)
    print(password)

    client = boto3.client(
        'cognito-idp',
        aws_access_key_id='',
        aws_secret_access_key='',
        config=Config(signature_version='s3v4')
    )
    try:
        response = client.sign_up(
            ClientId='',
            Username=username,
            Password=password,
            UserAttributes=[
                {
                    'Name': 'email',
                    'Value': username
                },
            ],
            ValidationData=[
                {
                    'Name': 'string',
                    'Value': 'string'
                },
            ],
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
    except:
        messagebox.showinfo(" ERROR ", "Error creating Account", icon="warning")



