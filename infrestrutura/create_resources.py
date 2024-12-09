import boto3
import json

def create_resources(config_file):
    with open(config_file) as file:
        config = json.load(file)
    
    s3 = boto3.client('s3')
    sns = boto3.client('sns')
    sqs = boto3.client('sqs')

    # Create S3 bucket
    s3.create_bucket(Bucket=config['s3_bucket'])
    print(f"S3 bucket {config['s3_bucket']} created.")

    # Create SNS topic
    sns_topic = sns.create_topic(Name=config['sns_topic'])
    sns_arn = sns_topic['TopicArn']
    print(f"SNS topic {config['sns_topic']} created.")

    # Create SQS queue
    sqs_queue = sqs.create_queue(QueueName=config['sqs_queue'])
    sqs_url = sqs_queue['QueueUrl']
    print(f"SQS queue {config['sqs_queue']} created.")

    # Subscribe SQS to SNS
    sns.subscribe(TopicArn=sns_arn, Protocol='sqs', Endpoint=sqs_url)
    print(f"Subscribed {config['sqs_queue']} to {config['sns_topic']}.")

if __name__ == "__main__":
    create_resources("config.json")
