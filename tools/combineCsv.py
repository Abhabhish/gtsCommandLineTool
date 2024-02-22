import pandas as pd
import os

def combine_csv_files():
    source = input("Enter path to all csv files:\n>>")
    destination = input("Enter the destination path:\n>>")
    
    all_files = os.listdir(source)
    
    csv_files = [f for f in all_files if f.endswith('.csv')]
    
    df_list = []
    
    for csv in csv_files:
        file_path = os.path.join(source, csv)
        try:
            df = pd.read_csv(file_path)
            df_list.append(df)
    
        except UnicodeDecodeError:
            try:
                df = pd.read_csv(file_path, sep='\t', encoding='utf-16')
                df.list_append(df)
            except Exception as e:
                print(f"Could not read file {csv} because of error: {e}")
        except Exception as e:
            print(f"Could not read file {csv} because of error: {e}")
    
    big_df = pd.concat(df_list, ignore_index=True)
    
    output_file_path = os.path.join(destination, 'combined_file.csv')
    
    big_df.to_csv(output_file_path, index=False)
    
    print(f"Combined the csv files in {destination}")