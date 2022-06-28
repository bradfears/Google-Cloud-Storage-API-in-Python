import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '<credential file name>.json'

storage_client = storage.Client()

"""
Download Files
"""
def download_file_from_bucket(blob_name, file_path, bucket_name):
	try:
		bucket = storage_client.get_bucket(bucket_name)
		blob = bucket.blob(blob_name)
		with open(file_path, 'wb') as f:
			storage_client.download_blob_to_file(blob, f)
		return True

	except Exception as e:
		print(e)
		return False

bucket_name = '<bucket_name>'
download_file_from_bucket('<soruce blob file name>', os.path.join(os.getcwd(), '<destination blob file name>'), bucket_name)
