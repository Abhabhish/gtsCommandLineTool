import pandas as pd
import os
import shutil

def move_with_segregation():

    csv_path = input("Enter the path of the CSV file:\n>>")
    source = input("Enter the source:\n>>")
    destination = input("Enter destination:\n>>")
    
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"Error: CSV file not found at {csv_path}")

    filename_column = df.columns[0]

    parameter_columns = [col for col in df.columns if col != filename_column]

    for index, row in df.iterrows():
        file_name = row[filename_column]

        source_path = os.path.join(source, file_name)

        if not os.path.exists(source_path):
            print(f"Error: File {file_name} not found in {source}. Skipping")
            continue

        destination_subfolder = os.path.join(destination, "_".join(str(row[col]) for col in parameter_columns))

        os.makedirs(destination_subfolder, exist_ok=True)

        destination_path = os.path.join(destination_subfolder, file_name)

        try:
            shutil.move(source_path, destination_path)
            print(f"Moved: {file_name} ----> {destination_subfolder}")
        except FileNotFoundError:
            print(f"Error: File {file_name} not found in {source}. Skipping.")