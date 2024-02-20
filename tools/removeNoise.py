import os
from audoai.noise_removal import NoiseRemovalClient
import csv
from concurrent.futures import ThreadPoolExecutor

def remove_noise():
    api_key = '6166bb920cc5f67c9b5295344d071eec'

    input_option = input("How would you like to input the audio file names?\n(a) Manually enter\n(b) Paste multiple names\n(c) Import from a CSV file\n\n>>>")

    noise_removal = NoiseRemovalClient(api_key=api_key)

    audio_files_to_be_cleaned = {}

    if input_option == 'a':
        print("Enter the audio file names: ")

        while True:
            current_name = input("Enter the name of audio files: ")
            if not current_name:
                break
            else:
                audio_files_to_be_cleaned[current_name] = True

    elif input_option == 'b':
        print("Paste the audio files: (format -> old_file_name new_file_name)")
        user_input = input(">> ")

        audio_files_to_be_cleaned = {pair.split()[0]: True for pair in user_input.split("\n") if pair}

    elif input_option == 'c':
        csv_file_path = input("Enter the path to CSV file:\n>>")

        try:
            with open(csv_file_path, newline='', encoding='utf-8') as csv_file:
                reader = csv.reader(csv_file)
                audio_files_to_be_cleaned = {row[0].strip(): True for row in reader if row}
        
        except FileNotFoundError:
            print(f"Error: CSV file not found at {csv_file_path}")
            return
    
    else:
        print("Invalid option. Enter 'a', 'b', or 'c'.")
        return

    source_directory = input("Enter the source directory containing the audio files:\n>>")
    
    with ThreadPoolExecutor() as executor:
        futures = []

        for root, dirs, files in os.walk(source_directory):
            for file in files:
                if file in audio_files_to_be_cleaned:
                    audio_path = os.path.join(root, file)

                    cleaned_path = os.path.join(root, f"cleaned_{file}")
                    audio_result = noise_removal.process(audio_path)
                    audio_result.save(cleaned_path)

                    print(f"Noise removed and saved: {audio_path} ----> {cleaned_path}")

        for future in futures:
            future.result()