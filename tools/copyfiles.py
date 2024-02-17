import os
import shutil

def copy():
    files_to_be_copied = []

    while True:
        i = input('Enter the file names to be copied:\n>>')
        if i== '':
            break
        else:
           files_to_be_copied.append(i)

    source = input('Enter Source:\n>>')
    destination = input('Enter destination:\n>>')

    for root,dirs,files in os.walk(source):
        for file in files:
            if file in files_to_be_copied:
               old_file_path = os.path.join(root,file)
               new_file_path = os.path.join(destination,file)
               if not os.path.exists(new_file_path):
                  shutil.copy(old_file_path,new_file_path)
                  print(f'Copied: {old_file_path} ---> {new_file_path}')
