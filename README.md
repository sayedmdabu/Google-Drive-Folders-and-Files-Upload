# Repository Name
Google-Drive-Folders-and-Files-Upload

# Description
A Python script for automating the upload of local directories and their files to Google Drive using the Google Drive API. Authenticate via a service account and upload files seamlessly to a specified Google Drive folder.

# README

## Google-Drive-Folders-and-Files-Upload

**Google-Drive-Folders-and-Files-Upload** is a Python script designed to simplify the process of uploading local folders and their files to Google Drive using the Google Drive API. This script leverages a service account for authentication.

### Features
- Authenticate with Google Drive API using a service account.
- Create folders in Google Drive corresponding to local directories.
- Upload all files within local directories to the created Google Drive folders.
- Error handling for smooth execution.

### Prerequisites
- Python 3.x
- Google service account JSON file (download from Google Cloud Console).

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/sayedmdabu/Google-Drive-Folders-and-Files-Upload.git
    cd Google-Drive-Folders-and-Files-Upload
    ```

2. Install required dependencies:
    ```bash
    pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
    ```

3. Place your service account JSON file in the project directory and update the `SERVICE_ACCOUNT_FILE` variable in the script with its filename.

### Usage

1. Define the list of local directories to upload:
    ```python
    output_dirs = ["example_dir1", "example_dir2"]
    ```
    Replace with the actual directory names.

2. Set the Google Drive parent folder ID where the directories will be uploaded:
    ```python
    google_drive_folder_id = "your_google_drive_folder_id"
    ```
    Replace with the actual folder ID from Google Drive.

3. Run the script:
    ```bash
    python upload_to_drive.py
    ```

### Script Breakdown

- **Authentication:**
  Uses the service account credentials to authenticate with Google Drive API.

- **Folder Creation:**
  Creates folders in Google Drive to mirror the local directory structure.

- **File Upload:**
  Uploads individual files from local directories to the corresponding Google Drive folders.

### Notes
- Ensure the service account has the required permissions to access and modify the target Google Drive folder.
- Avoid hardcoding sensitive credentials; consider using environment variables.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
Contributions and issues are welcome!

