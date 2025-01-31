import os
fileType = '.mp4'

anyFile = os.listdir('D:\VD\XV250125')
for file in anyFile:
    if file.endswith(fileType):
        print(file)

