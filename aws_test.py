import boto3

aws_access_ke_id = "AKIARHVA2Y7XQWSUCNGC",
aws_secret_access_key = "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"

# Let's use Amazon S3
s3 = boto3.resource('s3', aws_access_key_id="AKIARHVA2Y7XQWSUCNGC",
                    aws_secret_access_key="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")
for bucket in s3.buckets.all():
    print(bucket.name)

data = open("aws_test.py", 'rb')
s3.Bucket('aritrasnowball').put_object(Key='test_file.py', Body=data)

print("file uploaded!!!")
