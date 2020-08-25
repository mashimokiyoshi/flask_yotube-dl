from flask import make_response
import subprocess
import os

class download:
    def __init__(self, url, filename, ismp3):
        self.url = url
        self.filename = filename
        self.ismp3 = ismp3

    def execute(self):

        args = ['youtube-dl', self.url, '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]']
        res = subprocess.check_call(args)
        
        for file in os.listdir():
            base, ext = os.path.splitext(file)
            if ext == '.mp4':
                downloadFileNameMp4 = file

        response = make_response()
        response.data = open(downloadFileNameMp4, "rb").read()
        response.headers['Content-Disposition'] = 'attachment; filename=' + self.filename + '.mp4'

        return response