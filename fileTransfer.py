#
#
#               this code transfers files from folder a to folder b
#
#
#
import shutil
import os

#the source of the files (folder a)
source = '/Users/joybe/Desktop/FolderA/'

#destination for files from source (folder b)
destination = '/Users/joybe/Desktop/FolderB/'

files = os.listdir(source)
for i in files:
        shutil.move(source+i, destination)
