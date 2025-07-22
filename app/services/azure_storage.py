import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

AZURE_CONNECTION_STRING = os.getenv('AZURE_CONNECTION_STRING')
CONTAINER_NAME = os.getenv('AZURE_CONTAINER_NAME', 'your-container-name')

blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

def upload_file_to_blob(file_path, blob_name):
    with open(file_path, 'rb') as data:
        container_client.upload_blob(name=blob_name, data=data, overwrite=True)
    return f"Uploaded {blob_name} to Azure Blob Storage."

def download_file_from_blob(blob_name, download_path):
    blob_client = container_client.get_blob_client(blob_name)
    with open(download_path, 'wb') as download_file:
        download_file.write(blob_client.download_blob().readall())
    return f"Downloaded {blob_name} from Azure Blob Storage." 