import os
import shutil
import dropbox
class TransferData :
    def _init_(self, access_token) :
        self.access_token = access_token
    
    def upload_file(self, file_from, file_to) :
        dbx = dropbox.Dropbox(self.access_token)
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(),file_to)

path = "./test"
access_token="yTJQjgRsNhAAAAAAAAAAAaeTP99qzz2GEFlAzmmWi81mw9PTkDjARImV0wUmAjuV"
uploadFolder = TransferData(access_token)
for root, dirs, files in os.walk(path) :
    for name in files :
        filePath = os.path.join(root, name)
        serverPath = filePath
        uploadFolder.upload_file(filePath,serverPath)

    for name in dirs :
        filePath = os.path.join(root, name)
        serverPath = filePath
        uploadFolder.upload_file(filePath,serverPath)
print("\033[1;32mFolder Uploaded :)")