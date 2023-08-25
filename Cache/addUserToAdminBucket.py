from itertools import islice
import boto3
from botocore.client import Config

def main(email):

    domain = email.split('@')[0]



    f = open("%s.txt" % domain, "w+")
    #f = open("name.txt", "w+")
    #f.write('Hello')
    f.write(domain)

    f.close()

    BUCKET_NAME = 'admincachebucket2020'

    data = open('%s.txt' %domain, 'rb')
    #data = open("name.txt", "rb")
    # file = open('{0}.txt'.format(data[0], "w+"))

    # file.writelines(domain)
    #f = open('%s.txt' % domain, 'wb')
    #file.close()

    s3 = boto3.resource(
    's3',
    aws_access_key_id='AKIAJCQDHR55SMLULW3A',
    aws_secret_access_key='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',
    config=Config(signature_version='s3v4')
    )

    # saves the file to s3 bucket
    s3.Bucket(BUCKET_NAME).put_object(Key='%s.txt' % domain, Body=data)

    #s3.Bucket(BUCKET_NAME).put_object(Key="name.txt", Body=data)
    print("File Uploaded!")

if __name__ == '__main__':
    main()
