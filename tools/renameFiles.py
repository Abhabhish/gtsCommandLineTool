import os
import shutil
import csv

def rename():
    files_to_be_renamed = {}

    input_option = input("How would you like to input the file name?\n(a) Manually enter the file names\n(b) Import from CSV file\n\n>>>")

    if input_option == 'a':
        print("Enter the file names to be renamed: ")

        while True:
            current_name = input("Enter the current file name:\n>>")
            if not current_name:
                break
            else:
                new_name = input(f"Enter the new file name for {current_name}:\n>>")
                files_to_be_renamed[current_name] = new_name.strip()

    elif input_option == 'b':
        csv_file_path = input("Enter the path to the CSV file containing the new file names:\n>>")
        try:
            with open(csv_file_path, newline='', encoding='utf-8') as csv_file:
                reader = csv.reader(csv_file)
                files_to_be_renamed = {row[0].strip(): row[1].strip() for row in reader if row}
        
        except FileNotFoundError:
            print(f"Error: CSV file not found at {csv_file_path}")
            return
    else:
        print("Invalid option. Enter 'a' or 'b'.")
        return

    source = input("Enter Source:\n>>")

    for root, dirs, files in os.walk(source):
        for file in files:
            if file in files_to_be_renamed:
                old_file_path = os.path.join(root, file)

                new_file_name = files_to_be_renamed[file]
                new_file_path = os.path.join(root, new_file_name)

                if os.path.exists(new_file_path):
                    print(f"Error: File name already exist.")
                else:
                    os.rename(old_file_path, new_file_path)
                    print(f"Renamed: {old_file_path} ----> {new_file_path}")