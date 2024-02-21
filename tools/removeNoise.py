import os
from audoai.noise_removal import NoiseRemovalClient
import csv
from concurrent.futures import ThreadPoolExecutor

def process_audio(audio_files_to_be_cleaned):

    api_key = '6166bb920cc5f67c9b5295344d071eec'

    noise_removal = NoiseRemovalClient(api_key=api_key)

    source_directory = input("Enter the source directory containing audio files:\n>> ")

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = []

        for root, dirs, files in os.walk(source_directory):
            for file in files:
                if file in audio_files_to_be_cleaned:
                    audio_path = os.path.join(root, file)

                    cleaned_path = os.path.join(root, f"cleaned_{file}")

                    futures.append(executor.submit(process_single_audio, noise_removal, audio_path, cleaned_path))

        for future in futures:
            future.result()

def process_single_audio(noise_removal, audio_path, cleaned_path):
    audio_result = noise_removal.process(audio_path)
    audio_result.save(cleaned_path)
    print(f"Noise: {audio_path} ----> {cleaned_path}")

def remove_noise():

    input_option = input("How would you like to input the audio file names?\n(a) Manually enter\n(b) Paste names\n(c) Import from CSV\n\n>> ")

    audio_files_to_be_cleaned = {}

    if input_option == 'a':
        print("Enter the audio file names to be cleaned (one by one): ")

        while True:
            current_name = input("Enter the current audio file name (press Enter to finish):\n>>")
            if not current_name:
                break
            else:
                audio_files_to_be_cleaned[current_name] = True

    elif input_option == 'b':
        print("Paste the audio file names to be cleaned in this format:\n(old_audio_file_name1) (new_audio_file_name1)\n(old_audio_file_name2) (new_audio_file_name2)\n...etc")
        user_input = input(">> ")

        audio_files_to_be_cleaned = {pair.split()[0]: True for pair in user_input.split("\n") if pair}
        
    elif input_option == 'c':
        csv_file_path = input("Enter the path to the CSV file containing the audio file names:\n>>")
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

    process_audio(audio_files_to_be_cleaned)