import os
import csv

def delete():

    # Create a list to store the files to be deleted
    files_to_be_deleted = []

    input_option = input("How would you like to input the file names?\n(a) Manually enter the file names\n(b) Import from CSV file\n\n>>>")

    # If manual input option is chosen
    if (input_option == 'a'):
        print("Enter the file names to be deleted: ")

        while True:
            i = input(">> ")
            if not i:
                break
            else:
                files_to_be_deleted.append(i.strip()) # Append the files in the list

    # If CSV input option is chosen
    elif (input_option == 'b'):
        csv_file_path = input("Enter the path to CSV file:\n>>")
        try:
            with open(csv_file_path, newline='', encoding='utf-8') as csv_file:
                reader = csv.reader(csv_file)
                files_to_be_deleted = [row[0].strip() for row in reader if row]
        
        except FileNotFoundError:
            print(f"Error: CSV file not found at {csv_file_path}")
            return

    else:
        print("Invalid option. Enter 'a' or 'b'")
        return 

    # Enter the source path of files
    source = input("Enter the file source: ")

    # Iterate through the source folders
    for root, dirs, files in os.walk(source):
        for file in files:
            if file in files_to_be_deleted:
                file_path = os.path.join(root, file)
                if os.path.exists(file_path):
                    os.remove(file_path) # Delete the required files
                    print(f"Deleted file: {file_path}")