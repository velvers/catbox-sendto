import requests
import sys
import pyperclip
from plyer import notification

def upload_to_catbox(file_path):
    print(f"uploading file: {file_path}")  # debug shit
    url = 'https://catbox.moe/user/api.php'
    userhash = '####'  # userhash go here
    files = {'fileToUpload': open(file_path, 'rb')}
    data = {'reqtype': 'fileupload', 'userhash': userhash}

    response = requests.post(url, files=files, data=data)
    if response.status_code == 200:
        file_url = response.text.strip()
        print(f"upload successful: {file_url}")  # debug shit
        pyperclip.copy(file_url)
        notification.notify(
            title="catbox",
            message=f"file uploaded successfully :3 {file_url}",
            timeout=5  # duration in seconds
        )
    else:
        print(f"couldnt upload file (fuck): {response.status_code} - {response.text}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("no file provided, provide a file as an argument")
    else:
        file_path = sys.argv[1]
        print(f"received file path: {file_path}")  # debug shit
        upload_to_catbox(file_path)
