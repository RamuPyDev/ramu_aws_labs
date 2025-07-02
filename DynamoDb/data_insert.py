import boto3
import json
from botocore.exceptions import ClientError

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Change region as needed

# Specify your table name
table_name = 'Customers'
table = dynamodb.Table(table_name)

# Load JSON data
with open('data.json') as f:
    items = json.load(f)
print(len(items))
# Batch write (max 25 items per batch)
with table.batch_writer() as batch:
    for item in items:
        try:
            batch.put_item(Item=item)
            print(f"Inserted: {item}")
        except ClientError as e:
            print(f"Error inserting {item}: {e.response['Error']['Message']}")
