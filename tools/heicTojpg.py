from PIL import Image # pip install pillow
from pillow_heif import register_heif_opener # pip install pillow-heif
import os

register_heif_opener() # Call to work with HEIC/HEIF formats

def heic_to_jpg():

    # Setup a list to store the file names
    files_to_be_converted = []

    input_option = input("How would you like to input the file names?\n(a) Manually enter file names\n(b) Paste file names\n(c) Import from CSV file\n\n>>>")

    # Enter the source
    source = input("Enter source:\n>>")

    # Enter the destination
    destination = input("Enter destination:\n>>")

    # If manual input option is chosen
    if input_option == 'a':
        print("Enter the file names: ")

        while True:
            current_name = input("Enter the current file name:\n>>")

            if not current_name:
                break
            else:
                convert_heic_to_jpg(os.path.join(source, current_name), destination)

    # If paste multiple files name is chosen
    elif input_option == 'b':
        print("Paste file names:")

        while True:
            user_input = input(">> ").strip()

            if not user_input:
                break

            files_to_be_converted.append(os.path.join(source, user_input)) 

            for file_name in files_to_be_converted:
                convert_heic_to_jpg(os.path.join(source, file_name), destination)

    # If import from CSV option is chosen
    elif input_option == 'c':
        csv_file_path = input("Enter the path to the CSV file containing the file names:\n>>")
        try:
            with open(csv_file_path, newline='', encoding='utf-8') as csv_file:

                for row in csv_file:
                    convert_heic_to_jpg(os.path.join(source, row.strip()), destination)
        
        except FileNotFoundError:
            print(f"Error: CSV file not found at {csv_file_path}")
            return

    else:
        print("Invalid option. Enter 'a', 'b', or 'c'.")
        return


def convert_heic_to_jpg(source, destination):
    try:
        with Image.open(source) as img:
            rgb_img = img.convert("RGB") # Convert to RGB
            jpg_path = os.path.join(destination, os.path.splitext(os.path.basename(source))[0] + ".jpg") # Setup jpg path
            rgb_img.save(jpg_path) # Save as JPG

            print(f"Converted: {source} ----> {jpg_path}")

    except Exception as e:
        print(f"Error processing {source}: {e}")