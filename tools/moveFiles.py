import os
import shutil

def move():
    # Create an empty list to store file names
    files_to_be_moved = []

    # Input file names to be moved, break if the input is empty
    while True:
        i = input('Enter the file names to be moved (press Enter to finish):\n>>')
        if i == '':
            break
        else:
            files_to_be_moved.append(i)

    # Input source and destination directories
    source = input('Enter Source:\n>>')
    destination = input('Enter Destination:\n>>')

    # Traverse the source directory
    for root, dirs, files in os.walk(source):
        for file in files:
            # Check if the file is in the list of files to be moved
            if file in files_to_be_moved:
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.join(destination, file)
                # Check if the file does not exist in the destination
                if not os.path.exists(new_file_path):
                    # Move the file and print the message
                    shutil.move(old_file_path, new_file_path)
                    print(f'Moved: {old_file_path} ---> {new_file_path}')