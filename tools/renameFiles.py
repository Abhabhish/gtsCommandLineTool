import os
import shutil
import csv

def rename():

    # Create a dictionary to store the files to be renamed
    files_to_be_renamed = {}

    input_option = input("How would you like to input the file names?\n(a) Manually enter the file names one by one\n(b) Paste copied pairs of old and new file names.\n(c) Import pairs from a CSV file\n\n>>>")

    # If manual input option is chosen
    if input_option == 'a':
        
        print("Enter the file names: ")
        
        while True:
            current_name = input("Enter the current file name:\n>>")
            if not current_name:
                break
            else:
                new_name = input(f"Enter the new file name:\n>>")
                files_to_be_renamed[current_name] = new_name.strip() # Replace current name with new one
    
    # If pasting in pairs in the terminal option is chosen
    elif input_option == 'b':
        
        print("Paste pairs. Enter on new line to finish")

        while True:
            user_input = input(">> ").strip()

            if not user_input:
                break
            
            names = user_input.split()

            # Run only if the input is in pairs, else give error
            if len(names) == 2:
                old_name, new_name = names
                files_to_be_renamed[old_name] = new_name
            else:
                print("Invalid input format, paste in pairs")

    # If CSV import option is chosen
    elif input_option == 'c':

        csv_file_path = input("Enter the path to the CSV file containing the new file names:\n(Sample format: 1st col -> old_file_name, 2nd col -> new_file_name)\n>>")

        try:
            with open(csv_file_path, newline='', encoding='utf-8') as csv_file:
                reader = csv.reader(csv_file)
                files_to_be_renamed = {row[0].strip(): row[1].strip() for row in reader if row}
        
        except FileNotFoundError:
            print(f"Error: CSV file not found at {csv_file_path}")
            return

    else:
        print("Invalid option. Enter 'a', 'b' or 'c.")
        return

    # Enter the source path
    source = input("Enter source:\n>>")

    # Iterate through the source folders
    for root, dirs, files in os.walk(source):
        for file in files:
            if file in files_to_be_renamed:
                old_file_path = os.path.join(root, file)

                new_file_name = files_to_be_renamed[file]
                new_file_path = os.path.join(root, new_file_name)

                if os.path.exists(new_file_path):
                    print(f"Error: File name already exists.")
                else:
                    os.rename(old_file_path, new_file_path) # Rename the required files
                    print(f"Renamed: {old_file_path} ----> {new_file_path}")