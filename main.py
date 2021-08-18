import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A2yrr7U2bH6CmEHP072nInY-MqBSWneYi-Iv6hlp-wyQWgbfjsglax7pZJVmlRlA5G3W6b221PlP3yHKT-dhqU0UIDqahY_UZWuakOX9_0oCUF-erwiWVmN_20GEHgdFEvX2Qvw'
    transferData = TransferData(access_token)

    file_from = '/Users/HP_BOOK_PRO/Desktop/c-101/test.txt'
    file_to = '/Users/HP_BOOK_PRO/Dropbox/test.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()