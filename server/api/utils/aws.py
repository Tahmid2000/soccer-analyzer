from .secrets import AWS_ACCESS_KEY, AWS_SECRET_KEY, BUCKET_NAME
import boto3


def memory_to_aws(data, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY,
                      aws_secret_access_key=AWS_SECRET_KEY)
    s3.put_object(Body=data, Bucket=BUCKET_NAME,
                  ContentType='image/png', Key=s3_file)
