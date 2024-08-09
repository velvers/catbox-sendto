# catbox-sendto
simple python script to make uploading to [catbox](https://catbox.moe/) faster
## features
    - upload a file to [catbox](https://catbox.moe/)
    - copies url to your clipboard
    - notification on successful file upload
## usage
    - right-click any file, select "Send to," and choose `catbox` to upload the file.
    - file will be uploaded to catbox.moe, and the url will be copied to your clipboard.
    - a windows notification will appear with the upload status.
## installation
1. **clone the repository**
    ```bash
    git clone https://github.com/velvers/catbox-sendto.git
    ```
2. **requirements**
    ```bash
    pip install -r requirements.txt
    ```
3. **add your userhash**
   ```python
    userhash = '####'  # userhash go here
   ```
4. **batch file**
    ```batch
    @echo off
    python "D:\path\to\your\catbox.py" %1
    ```
    - save this batch file as `catbox.bat` in your `send to` folder (`shell:sendto`)

4.5 **optional**
- make a shortcut for the batch file and save it as `&catbox` and add an icon (`catbox.ico`) to it (looks nicer imo)
