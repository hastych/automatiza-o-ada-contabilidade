import boto3
import os
from generate_file import generate_file

def upload_to_s3(bucket_name):
    s3 = boto3.client('s3')
    file_name, lines = generate_file()
    try:
        s3.upload_file(file_name, bucket_name, file_name)
        print(f"Uploaded {file_name} to bucket {bucket_name}.")
        return file_name, lines
    except Exception as e:
        print(f"Error uploading file: {e}")
    finally:
        os.remove(file_name)

if __name__ == "__main__":
    bucket_name = "your-s3-bucket-name"
    upload_to_s3(bucket_name)
