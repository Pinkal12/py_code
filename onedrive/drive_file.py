import requests
import json
import os


# Set the client ID, client secret, and tenant ID for your Azure AD app registration
client_id = 'a1911140-a9a3-4c78-8841-deb9aba08107'
client_secret = '0uF8Q~yJvw8SwWQsOP8NyVPnCCCefIYvdNP5jbK-'
tenant_id = 'b636e424-e0a8-4fff-81ba-2a126a7ce362'

# Set the path to your local file
file_path = '/home/hanuai/mygithub/py_code/onedrive/images.png'

# Set the OneDrive folder ID for the folder you want to upload to
folder_id = 'En4wppND3fZIiVPSyCkFWkABbU1PdrTemivzkrALMJ_dNg'

# Construct the URL for the Microsoft Graph API access token endpoint
token_url = 'https://login.microsoftonline.com/{0}/oauth2/v2.0/token'.format(tenant_id)

# Construct the data for the Microsoft Graph API access token request
token_data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': 'https://graph.microsoft.com/.default'
}

# Send the Microsoft Graph API access token request and get the access token
response = requests.post(token_url, data=token_data)
print(response.text)  # Print out the response text for debugging
access_token = json.loads(response.text)['access_token']

# Construct the URL for the OneDrive API upload endpoint
upload_url = 'https://graph.microsoft.com/v1.0/me/drive/items/{0}:/{1}:/content'.format(folder_id, os.path.basename(file_path))

# Set the headers for the OneDrive API upload request
upload_headers = {
    'Authorization': 'Bearer {0}'.format(access_token),
    'Content-Type': 'application/octet-stream'
}

# Open the local file and read its contents
with open(file_path, 'rb') as f:
    file_contents = f.read()

# Send the OneDrive API upload request and upload the file
response = requests.put(upload_url, headers=upload_headers, data=file_contents)

# Check the response to see if the upload was successful
if response.status_code == 201:
    print('The Upload successful')
else:
    print('The Upload failed ')
