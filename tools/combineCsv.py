import pandas as pd # pip install pandas
import os

def combine_csv_files():
    
    # Enter the source
    source = input("Enter path to all csv files:\n>>")

    # Enter the destination
    destination = input("Enter the destination path:\n>>")
    
    # List all files in source provided
    all_files = os.listdir(source)
    
    # check for CSV files
    csv_files = [f for f in all_files if f.endswith('.csv')]
    
    # Setup the dataframe list
    df_list = []
    
    # Iterate through the CSV files
    for csv in csv_files:
        file_path = os.path.join(source, csv)
        try:
            df = pd.read_csv(file_path) # Setup dataframe
            df_list.append(df) # Append to the dataframe list
    
        except UnicodeDecodeError:
            try:
                df = pd.read_csv(file_path, sep='\t', encoding='utf-16')
                df.list_append(df)
            except Exception as e:
                print(f"Could not read file {csv} because of error: {e}")
        except Exception as e:
            print(f"Could not read file {csv} because of error: {e}")
    
    big_df = pd.concat(df_list, ignore_index=True) # Merge the CSV contents
    
    output_file_path = os.path.join(destination, 'combined_file.csv') # Setup the output file path
    
    big_df.to_csv(output_file_path, index=False) # Save the merged file
    
    print(f"Combined the csv files in {destination}")