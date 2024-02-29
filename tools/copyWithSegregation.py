import pandas as pd # pip install pandas
import os
import shutil

def copy_with_segregation():

    # Input the CSV file path
    csv_path = input("Enter the path of the CSV file:\n(Sample format: 1st col -> file_name, other cols -> other parameters)\n>>")

    # Enter the source of files
    source = input("Enter the source:\n>>")

    # Enter the destination folder path
    destination = input("Enter destination:\n>>")
    
    # Create a dataframe for reading the CSV file
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:

        # Print an error statement if the CSV file is not found
        print(f"Error: CSV file not found at {csv_path}")

    # Setup filename column as the first column
    filename_column = df.columns[0]

    # Iterate through the columns
    parameter_columns = [col for col in df.columns if col != filename_column]

    # Iterate through the rows
    for index, row in df.iterrows():
        file_name = row[filename_column]

        # Create a source path
        source_path = os.path.join(source, file_name)

        # If the file is not present in the source path
        if not os.path.exists(source_path):
            print(f"Error: File {file_name} not found in {source}. Skipping")
            continue

        # Create the destination subfolders
        destination_subfolder = os.path.join(destination, "_".join(str(row[col]) for col in parameter_columns))
        os.makedirs(destination_subfolder, exist_ok=True)

        # Create the destination path
        destination_path = os.path.join(destination_subfolder, file_name)

        # Copy the contents in the subfolder
        try:
            shutil.copy(source_path, destination_path)
            print(f"Copied: {file_name} ----> {destination_subfolder}")
        except FileNotFoundError:

            # Give error if the file is not present
            print(f"Error: File {file_name} not found in {source}. Skipping.")