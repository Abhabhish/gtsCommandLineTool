import os
import shutil
import csv

def move():

    # Create a list of files to be moved
    files_to_be_moved = []


    input_option = input("How would you like to input the file names?\n(a) Manually enter the file names\n(b) Import from CSV file\n\n>>>")

    # If manual option is chosen
    if (input_option == 'a'):
        print("Enter the file names to be copied: ")

        while True:
            i = input(">> ")
            if not i:
                break
            else:
                files_to_be_moved.append(i.strip())

    # If import from CSV option is chosen
    elif (input_option == 'b'):
        csv_file_path = input("Enter the path to the CSV file: ")

        try:
            with open(csv_file_path, newline='', encoding='utf-8') as csv_file:
                reader = csv.reader(csv_file)
                files_to_be_moved = [row[0].strip() for row in reader if row]
        except FileNotFoundError:
            print(f"Error: CSV file not found at {csv_file_path}")
            return
    else:
        print("Invalid option. Enter 'a' or 'b'.")
        return

    # Enter the file source
    source = input("Enter file source:\n>>>")

    # Enter the destination folder
    destination = input("Enter file destination:\n>>>")

    # Iterate through the source folder
    for root, dirs, files in os.walk(source):
        for file in files:
            if file in files_to_be_moved:
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.join(destination, file)

                if not os.path.exists(new_file_path):

                    # Move the files
                    shutil.move(old_file_path, new_file_path)
                    print(f"Moved: {old_file_path} ----> {new_file_path}")