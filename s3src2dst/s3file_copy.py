import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    source_bucket = "s3rdarasrc"
    destination_bucket = "s3rdaradst"

    # Extract the object key from the event
    object_key = event['Records'][0]['s3']['object']['key']

    # URL encode the source object key
    copy_source = {'Bucket': source_bucket, 'Key': object_key}

    # Set up the parameters for the copy operation
    copy_params = {
        'Bucket': destination_bucket,
        'CopySource': copy_source,
        'Key': object_key
    }

    try:
        # Perform the copy operation
        result = s3.copy_object(**copy_params)
        print("S3 object copy successful. Response:", result)
    except Exception as e:
        print("Error copying object:", str(e))
