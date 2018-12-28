from __future__ import unicode_literals
import youtube_dl
import os

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'outtmpl': '/songs/%(title)s.mp3',
    'format': 'bestaudio/best',
    'noplaylist' : False,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

try:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        inputURL = input("Please Input Your Youtube URL: ")
        ydl.download([inputURL])
except Exception:
    pass

#os.system("python mp3Downloader/convertToMP3.py")
