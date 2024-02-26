import pandas as pd # pip install pandas
import os
import shutil

def move_with_segregation():

    # Input the CSV file path
    csv_path = input("Enter the path of the CSV file:\n>>")

    # Enter the source of the files
    source = input("Enter the source:\n>>")

    # Enter the destination path
    destination = input("Enter destination:\n>>")
    
    # Create a dataframe for reading the CSV file 
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        
        # Give error of the CSV file is not present
        print(f"Error: CSV file not found at {csv_path}")

    # Setup the first column as the filename column
    filename_column = df.columns[0]

    # Iterate through the columns
    parameter_columns = [col for col in df.columns if col != filename_column]

    # Iterate through the rows
    for index, row in df.iterrows():
        file_name = row[filename_column]

        # Create a source path
        source_path = os.path.join(source, file_name)

        # Give error if the file does not exist at source 
        if not os.path.exists(source_path):
            print(f"Error: File {file_name} not found in {source}. Skipping")
            continue

        # Create a subfolder to save the files
        destination_subfolder = os.path.join(destination, "_".join(str(row[col]) for col in parameter_columns))

        os.makedirs(destination_subfolder, exist_ok=True)

        # Setup the destination path
        destination_path = os.path.join(destination_subfolder, file_name)

        # Move the files
        try:
            shutil.move(source_path, destination_path)
            print(f"Moved: {file_name} ----> {destination_subfolder}")
        except FileNotFoundError:

            # Give error if file is not present
            print(f"Error: File {file_name} not found in {source}. Skipping.")