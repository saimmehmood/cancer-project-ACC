'''
	Before any use of this file you need to source the .sh file containing
	you credentials to the cloud.
'''
import os
import swiftclient.client
from os import listdir

# Connect to swift 
def new_connection():
	config = {'user':os.environ['OS_USERNAME'], 
	          'key':os.environ['OS_PASSWORD'],
	          'tenant_name':os.environ['OS_TENANT_NAME'],
	          'authurl':os.environ['OS_AUTH_URL']}

	conn = swiftclient.client.Connection(auth_version=2, **config)
	return conn

# Create new bucket
def new_bucket(conn, name):
	conn.put_container(name)
	return name
	
#list all buckets
def list_all(conn)
	(response, bucket_list) = conn.get_account()
	for bucket in bucket_list:
		print bucket['name']

# Upload files to the bucket. One single file or a directory can be uploaded
def upload_files_to_bucket(conn, bucket_name, file_or_directory):
	print "Starting upload"
	if os.path.exists(file_or_directory):
		files = None
		if os.path.isdir(file_or_directory):
			files = listdir(file_or_directory)
			print files
			for item in files:
				print item
				fd = file(file_or_directory + '/' + item)
				objContent = fd.read()
				object_id = conn.put_object(bucket_name, item, objContent)
		else:
			print file_or_directory
			fd = file(file_or_directory)
			objContent = fd.read()
			object_id = conn.put_object(bucket_name, file_or_directory, objContent)

# List all the items in a given container
def list_items_in_container(conn, bucket_name):
	container = conn.get_container(bucket_name)
	for item in container[1]:
		print item['name']

# Clear and remove bucket
def clean_and_remove(conn, bucket_name):
	container = conn.get_container(bucket_name)
	for item in container[1]:
		conn.delete_object(bucket_name, item['name'])
	conn.delete_container(bucket_name)
