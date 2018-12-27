import os,sys

folder = 'mp3Downloader/before_convert'

for filename in os.listdir(folder):
       infilename = os.path.join(folder,filename)

       if not os.path.isfile(infilename): continue
       oldbase = os.path.splitext(filename)
       newname = infilename.replace('.m4a', '.mp3')
       output = os.rename(infilename, newname)