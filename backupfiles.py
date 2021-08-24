import os
import shutil

source = input('Enter the source ')
destination = input('Enter the Destination ')
source = source+'/'
destination = destination +'/'

list_of_files = os.listdir(source)

for files in list_of_files:
    shutil.copy((source + files),destination)