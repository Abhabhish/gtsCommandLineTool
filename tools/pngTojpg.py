from PIL import Image
import os

def png_to_jpg():

    input_option = input("How would you like to input the file names?\n(a) Manually enter file names\n(b) Paste file names\n(c) Import from CSV file\n\n>>>")

    source = input("Enter source:\n>> ")
    destination = input("Enter destination:\n>> ")

    if input_option == 'a':
        print("Enter the file names: ")

        while True:
            current_name = input("Enter the current file name:\n>>")
            if not current_name:
                break
            else:
                convert_png_to_jpg(os.path.join(source, current_name), destination)

    elif input_option == 'b':
        print("Paste file names:")

        while True:
            user_input = input(">> ").strip()

            if not user_input:
                break

            files_to_be_converted.append(os.path.join(source, user_input))

            for file_name in files_to_be_converted:
                convert_heic_to_jpg(os.path.join(source, file_name), destination)

    elif input_option == 'c':
        csv_file_path = input("Enter the path to the CSV file containing the file names:\n>>")
        try:
            with open(csv_file_path, newline='', encoding='utf-8') as csv_file:

                for row in csv_file:
                    convert_png_to_jpg(os.path.join(source, row.strip()), destination)
        
        except FileNotFoundError:
            print(f"Error: CSV file not found at {csv_file_path}")
            return

    else:
        print("Invalid option. Enter 'a', 'b', or 'c'.")
        return

def convert_png_to_jpg(source, destination):
    try:
        with Image.open(source) as img:
            rgb_img = img.convert("RGB")
            jpg_path = os.path.join(destination, os.path.splitext(os.path.basename(source))[0] + ".jpg")
            rgb_img.save(jpg_path)
            print(f"Converted: {source} ----> {jpg_path}")

    except Exception as e:
        print(f"Error processing {source}: {e}")
