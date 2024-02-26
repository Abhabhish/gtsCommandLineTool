import os
import shutil
import csv

def copy():
    # Create a list for files
    files_to_be_copied = []

    input_option = input("How would you like to input the file names?\n(a) Manually enter the file names\n(b) Import from CSV file\n\n>>>")

    # If manual option is chosen
    if (input_option == 'a'):
        print("Enter the file names to be copied: ")
        
        while True:
            i = input(">> ")
            if not i:
                break
            else:
                files_to_be_copied.append(i.strip())

    # If CSV file import option is chosen
    elif (input_option == 'b'):
        csv_file_path = input("Enter the path to the CSV file: ")
        try:
            with open(csv_file_path, newline='', encoding='utf-8') as csv_file:
                reader = csv.reader(csv_file)
                files_to_be_copied = [row[0].strip() for row in reader if row]
        except FileNotFoundError:
            print(f"Error: CSV file not found at {csv_file_path}")
            return
    
    else:
        print("Invalid option. Enter 'a' or 'b'.")
        return

    # Enter the file source
    source = input("Enter file Source:\n>>>")

    # Enter the destination folder
    destination = input("Enter file Destination:\n>>>")

    # Iterate through the source folders
    for root, dirs, files in os.walk(source):
        for file in files:
            if file in files_to_be_copied:
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.join(destination, file)

                if not os.path.exists(new_file_path):

                    # Copy using shutil function
                    shutil.copy(old_file_path, new_file_path)
                    print(f"Copied: {old_file_path} ----> {new_file_path}")