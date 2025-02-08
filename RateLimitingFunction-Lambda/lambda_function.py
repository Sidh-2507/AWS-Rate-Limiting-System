import json
import time
import boto3
from botocore.exceptions import ClientError

# AWS DynamoDB setup
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('RateLimitTableWithSortKey')

MAX_REQUESTS = 2  # Testing with lower limits
TIME_WINDOW = 10  # 10 seconds

def lambda_handler(event, context):
    ip = event['requestContext']['identity']['sourceIp']
    current_time = int(time.time())

    print(f"Processing request for IP: {ip} at {current_time}")

    try:
        response = table.get_item(Key={'ip': ip})
        item = response.get('Item', {})
        
        if item:
            request_count = item['request_count']
            last_request_time = item['last_request_time']
            
            print(f"Existing data - Count: {request_count}, Last Time: {last_request_time}")

            if current_time - last_request_time > TIME_WINDOW:
                request_count = 0  # Reset after time window
            
            if request_count >= MAX_REQUESTS:
                print("🚫 Too many requests! Returning 429")
                return {
                    'statusCode': 429,
                    'body': json.dumps('Rate limit exceeded. Try again later.')
                }
            
            request_count += 1
        else:
            request_count = 1
        
        # Save updated request count
        table.put_item(
            Item={'ip': ip, 'request_count': request_count, 'last_request_time': current_time}
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Request allowed')
        }

    except ClientError as e:
        print(f"Error accessing DynamoDB: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
