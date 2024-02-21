import os
import requests
from concurrent.futures import ThreadPoolExecutor
import csv

def download_file(link, destination_directory):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            file_name = os.path.basename(link)
            file_path = os.path.join(destination_directory, file_name)

            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded: {link} ----> {file_path}")
        else:
            print(f"Failed to download: {link}")
    
    except Exception as e:
        print(f"Error downloading {link}: {e}")

def download_files():
    links_to_download = []

    input_option = input("How would you like to input links?\n(a) One by one\n(b) Multiple\n(c) Import from a CSV file\n\n>>>")

    if input_option == 'a':
        print("Enter the links: ")
        while True:
            current_link = input("Paste a link: (enter to finish)\n>>")
            if not current_link:
                break
            else:
                links_to_download.append(current_link.strip())
    
    elif input_option == 'b':
        print("Paste the links: ")
        user_input = input(">> ")
        links_to_download = [link.strip() for line in user_input.split('\n') if line.strip()]

    elif input_option == 'c':
        csv_file_path = input("Enter path to the CSV file:\n>>")

        try:
            with open(csv_file_path, newline='', encoding='utf-8') as csv_file:
                reader = csv.reader(csv_file)
                links_to_download = [row[0].strip() for row in reader if row]
        
        except FileNotFoundError:
            print(f"Error: CSV file not found at {csv_file_path}")
            return
    
    else:
        print("Invalid option. Enter 'a', 'b', or 'c'.")
        return

    destination_directory = input("Enter Destination folder:\n>>")

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = []
        for link in links_to_download:
            futures.append(executor.submit(download_file, link, destination_directory))

        for future in futures:
            future.result()