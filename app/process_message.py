import boto3
import json
from database import save_to_database

def process_message(sqs_queue, bucket_name):
    sqs = boto3.client('sqs')
    s3 = boto3.client('s3')
    
    response = sqs.receive_message(QueueUrl=sqs_queue, MaxNumberOfMessages=1)
    
    if 'Messages' in response:
        for message in response['Messages']:
            body = json.loads(message['Body'])
            file_name = body['Records'][0]['s3']['object']['key']
            
            # Download file from S3
            s3.download_file(bucket_name, file_name, file_name)
            
            # Count lines in file
            with open(file_name, 'r') as file:
                lines = sum(1 for _ in file)
            
            # Save to database
            save_to_database(file_name, lines)
            
            # Delete processed message
            sqs.delete_message(QueueUrl=sqs_queue, ReceiptHandle=message['ReceiptHandle'])
            print(f"Processed and saved {file_name} with {lines} lines.")
    else:
        print("No messages in queue.")

if __name__ == "__main__":
    process_message("your-sqs-queue-url", "your-s3-bucket-name")
