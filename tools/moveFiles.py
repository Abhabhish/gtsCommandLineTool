import os
import shutil

def move():
    files_to_be_moved = []

    while True:
        i = input('Enter the file names to be moved:\n>>')
        if (i == ''):
            break
        else:
            files_to_be_moved.append(i)

    source = input('Enter Source:\n>>')
    destination = input('Enter Destination:\n>>')

    for root, dirs, files in os.walk(source):
        for file in files:
            if file in files_to_be_moved:
                old_file_path = os.path.join(root,file)
                new_file_path = os.path.join(destination,file)
                if not os.path.exists(new_file_path):
                    shutil.move(old_file_path, new_file_path)
                    print(f'Moved: {old_file_path} ---> {new_file_path}')