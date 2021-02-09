# import the required libraries
from __future__ import print_function
import pickle
import os.path
import io
import shutil
import requests
from mimetypes import MimeTypes
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload

global SCOPES

# Define the scopes
SCOPES = ['https://www.googleapis.com/auth/drive']

# Variable creds will
# store the user access token.
# If no valid token found
# we will create one.
creds = None

# The file token.pickle stores the
# user's access and refresh tokens. It is
# created automatically when the authorization
# flow completes for the first time.
print("DEBUG > os.path:\n\t", os.path)
# Check if file token.pickle exists
if os.path.exists('token.pickle'):
	# Read the token from the file and
	# store it in the variable creds
	with open('token.pickle', 'rb') as token:
		creds = pickle.load(token)

# If no valid credentials are available,
# request the user to log in.
if not creds or not creds.valid:
	# If token is expired, it will be refreshed,
	# else, we will request a new one.
	if creds and creds.expired and creds.refresh_token:
		creds.refresh(Request())
	else:
		flow = InstalledAppFlow.from_client_secrets_file(
			'credentials.json', SCOPES)
		creds = flow.run_local_server(port=0)
	# Save the access token in token.pickle
	# file for future usage
	with open('token.pickle', 'wb') as token:
		pickle.dump(creds, token)

# Connect to the API service
service = build('drive', 'v3', credentials=creds)


def main_function():
	get_files()
	i = int(input("Enter your choice: 1 - Download file, 2- Upload File, 3- Exit.\n"))

	if i == 1:
		f_id = input("Enter file id: ")
		f_name = input("Enter file name: ")
		FileDownload(f_id, f_name)
	elif i == 2:
		f_path = input("Enter full file path: ")
		FileUpload(f_path)
	else: exit()


def get_files():
	# request a list of first N (pageSize) files or
	# folders with name and id from the API.
	results = service.files().list(pageSize=100, fields="files(id, name)").execute()
	items = results.get('files', [])

	# print a list of files
	print("Here's a list of files: \n")
	print(*items, sep="\n", end="\n\n")
	print("\nRESULTS DEBUG PRINT OUT>\n", results)
	return items


def FileDownload(file_id, file_name):
	request = service.files().get_media(fileId=file_id)
	fh = io.BytesIO()

	# Initialise a downloader object to download the file
	downloader = MediaIoBaseDownload(fh, request, chunksize=204800)
	done = False

	try:
		# Download the data in chunks
		while not done:
			status, done = downloader.next_chunk()

		fh.seek(0)

		# Write the received data to the file
		with open(file_name, 'wb') as f:
			shutil.copyfileobj(fh, f)

		print("File Downloaded")
		# Return True if file Downloaded successfully
		return True
	except:
		# Return False if something went wrong
		print("Something went wrong.")
		return False


def FileUpload(filepath):
	# TODO: FILE NAME AND FILE TYPE...
	# splitting file path with '/' does not yet work
	# 	because windows will sometimes use '\' instead...
	# 	This also breaks MimeTypes().guess_type because
	# 	the name does not properly generate...
	# We will instead ask the user for the file name and
	# 	split by '.' to get the file type until this issue is resolved.

	# TODO: FILE NAME AND FILE TYPE...
	# Extract the file name out of the file path
	# name = filepath.split('/')[-1]

	# Ask the user to enter a file upload name.
	file_name = input("Enter the name you want the file to be uploaded as: ")

	# Find the MimeType of the file
	# TODO: FILE NAME AND FILE TYPE...
	# mimetype = MimeTypes().guess_type(name)[0]
	file_type = filepath.split('.')[-1]
	mimetype = MimeTypes().guess_type(file_type)[0]

	# create file metadata
	file_metadata = {'name': file_name}

	try:
		media = MediaFileUpload(filepath, mimetype=mimetype)

		# Create a new file in the Drive storage
		file = service.files().create(
			body=file_metadata, media_body=media, fields='id').execute()

		print("File Uploaded.")

	except:
		# Raise UploadError if file is not uploaded.
		raise UploadError("Can't Upload File.")


def hello_title_change(pram1, pram2):
	print("DEBUG > test function")
	print("\tpram1: ", pram1)
	print("\tpram2: ", pram2)
	return "hello"
