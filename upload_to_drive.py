from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build
import os  # Ensure the os module is imported for file operations

# Define the scope for accessing Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive']

# Path to the service account credentials JSON file
SERVICE_ACCOUNT_FILE = 'credentials.json'  # Replace with your actual service account JSON file

# Function to authenticate using the service account credentials
def authenticate():
    """
    Authenticates the application with Google Drive API using a service account.
    
    Returns:
        creds: The authenticated credentials object.
    """
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

# Function to upload folders and their files to Google Drive
def upload_folders_to_drive(parent_folder_id, output_dirs):
    """
    Uploads a list of local directories to a specified folder in Google Drive.

    Args:
        parent_folder_id (str): The ID of the parent folder in Google Drive.
        output_dirs (list): List of local directories to upload.
    """
    try:
        # Authenticate with Google Drive
        creds = authenticate()
        drive = build('drive', 'v3', credentials=creds)

        # Iterate over each local directory in the provided list
        for directory in output_dirs:
            directory_path = os.path.join(script_dir, directory)  # Construct the full path to the directory
            print(f"Uploading folder: {directory_path}")

            # Create a corresponding folder in Google Drive
            folder_metadata = {
                'name': directory,  # Name of the folder to be created in Google Drive
                'mimeType': 'application/vnd.google-apps.folder',  # Specify folder MIME type
                'parents': [parent_folder_id]  # Set the parent folder ID
            }
            folder = drive.files().create(body=folder_metadata, fields='id').execute()  # Create the folder
            folder_id = folder.get('id')  # Retrieve the created folder's ID
            print(f"Folder '{directory}' created on Google Drive with ID: {folder_id}")

            # Upload all files within the local directory to the created Drive folder
            for file_name in os.listdir(directory_path):
                file_path = os.path.join(directory_path, file_name)  # Full path to the file
                if os.path.isfile(file_path):  # Check if it's a file
                    print(f"Uploading file: {file_path}")
                    file_metadata = {
                        'name': file_name,  # File name in Google Drive
                        'parents': [folder_id]  # Set the parent folder ID
                    }
                    media = MediaFileUpload(file_path, resumable=True)  # Prepare the file for upload
                    try:
                        # Upload the file to Google Drive
                        uploaded_file = drive.files().create(
                            body=file_metadata,
                            media_body=media,
                            fields='id'
                        ).execute()
                        print(f"Uploaded file: {file_name}")
                    except Exception as e:
                        # Handle errors during file upload
                        print(f"Error uploading file {file_name}: {e}")
    except Exception as e:
        # Handle errors during the folder upload process
        print(f"Error in upload_folders_to_drive: {e}")

if __name__ == "__main__":
    # List of local output directories to be uploaded
    # Replace with your actual directory paths
    output_dirs = ["example_dir1", "example_dir2"]  # Add actual folder names here

    # Google Drive parent folder ID where the directories will be uploaded
    # Replace with your actual parent folder ID
    google_drive_folder_id = "your_google_drive_folder_id"

    # Upload the folders to Google Drive
    upload_folders_to_drive(google_drive_folder_id, output_dirs)

