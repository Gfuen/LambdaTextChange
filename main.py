import boto3
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    # Find text file
    if object_key.endswith('.txt'):
        # Download the file
        temp_file_path = f'/tmp/{object_key}'
        s3.download_file(bucket_name, object_key, temp_file_path)

        # Read 
        with open(temp_file_path, 'r') as file:
            file_content = file.read()

        # Replace "Hello World" 
        updated_content = file_content.replace('Hello World', 'Goodbye World')

        with open(temp_file_path, 'w') as file:
            file.write(updated_content)

        # Upload the file
        s3.upload_file(temp_file_path, bucket_name, object_key)

        return {
            'statusCode': 200,
            'body': f'Successfully updated {object_key} in {bucket_name}'
        }
    else:
        return {
            'statusCode': 200,
            'body': f'{object_key} is not a text file.'
        }
