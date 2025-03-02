import requests
import sys
import pyperclip
from plyer import notification
from tqdm import tqdm
from requests_toolbelt.multipart.encoder import MultipartEncoder, MultipartEncoderMonitor
import os


def upload_to_catbox(file_path):
    print(f"uploading file: {file_path}")  # debug shit
    url = 'https://catbox.moe/user/api.php'
    userhash = '####'  # userhash go here

    file_size = os.path.getsize(file_path)
    file_name = os.path.basename(file_path)

    with open(file_path, 'rb') as f:
        encoder = MultipartEncoder(
            fields={
                'reqtype': 'fileupload',
                'userhash': userhash,
                'fileToUpload': (file_name, f, 'application/octet-stream')
            }
        )

        with tqdm(total=file_size, unit='B', unit_scale=True, desc=file_name, ascii=True) as progress_bar:
            def progress_callback(monitor):
                progress_bar.update(monitor.bytes_read - progress_bar.n)

            monitor = MultipartEncoderMonitor(encoder, progress_callback)

            headers = {'Content-Type': monitor.content_type}
            response = requests.post(url, data=monitor, headers=headers)

    if response.status_code == 200:
        file_url = response.text.strip()
        print(f"upload successful: {file_url}")  # debug shit
        pyperclip.copy(file_url)
        notification.notify(
            title="catbox",
            message=f"file uploaded successfully :3 {file_url}",
            timeout=5
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
