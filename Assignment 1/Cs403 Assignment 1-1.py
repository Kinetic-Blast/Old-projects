import boto3

#file layout is
#AWS_ACCESS_KEY_ID
#AWS_SECRET_ACCESS_KEY

Keys = open ("awskeys.txt","r")
AWS_ACCESS_KEY_ID =Keys.readline().rstrip()
AWS_SECRET_ACCESS_KEY =Keys.readline().rstrip()
AWS_SESSION_TOKEN = Keys.readline().rstrip()

Name = input("What is your name?: ")
f = open(Name+".txt", "w")
f.write(Name)
f.close()


session = boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID,aws_secret_access_key=AWS_SECRET_ACCESS_KEY,aws_session_token=AWS_SESSION_TOKEN)
s3 = session.resource('s3')

data = open(Name+".txt", 'rb')
s3.Bucket('kineticbucket').put_object(Key=Name+".txt", Body=data)

obj = s3.Object('kineticbucket', Name+".txt")
body = obj.get()['Body'].read()

print(body)

bucket = s3.Bucket('kineticbucket')
for key in bucket.objects.all():
    key.delete()