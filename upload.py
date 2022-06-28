import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '<credential file name>.json'

storage_client = storage.Client()

"""
Upload Files
"""

def upload_to_bucket(blob_name, file_path, bucket_name):
	try:
		bucket = storage_client.get_bucket(bucket_name)
		blob = bucket.blob(blob_name)
		blob.upload_from_filename(file_path)
		return True

	except Exception as e:
		print(e)
		return False

file_path = r'<full path to files>'

upload_to_bucket('<soruce blob file name>', os.path.join(file_path, '<destination blob file name>'), '<bucket_name>')
