import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '<credential file name>.json'

storage_client = storage.Client()

"""
Create a New Bucket
"""
bucket_name = 'unique_bucket_name' # e.g., mybucket3421a
bucket = storage_client.bucket(bucket_name)
bucket.location = 'US'
bucket = storage_client.create_bucket(bucket)

"""
Print Bucket Detail
"""
vars(bucket)

"""
Accessing a Specific Bucket
"""
my_bucket = storage_client.get_bucket('<bucket_name>')


