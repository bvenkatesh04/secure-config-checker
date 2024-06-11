# src/checker.py
import boto3

def check_s3_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    for bucket in response['Buckets']:
        bucket_name = bucket['Name']
        acl = s3.get_bucket_acl(Bucket=bucket_name)
        for grant in acl['Grants']:
            if grant['Permission'] == 'FULL_CONTROL':
                print(f"Bucket {bucket_name} has FULL_CONTROL permissions")

if __name__ == "__main__":
    check_s3_buckets()

