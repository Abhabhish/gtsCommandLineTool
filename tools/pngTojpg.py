from PIL import Image
import os
import csv

def png_to_jpg():

    print("Choose the conversion method ->\n(a) Input source folder path\n(b) Import from a CSV file\n\n>>>")

    input_option = input(">> ")

    source = input("Enter source of image directory:\n>>")

    destination = input("Enter destination:\n>>")

    if input_option == 'a':

        for root, dirs, files in os.walk(source):
            for file in files:
                if file.lower().endswith('.png'):
                    convert_png_to_jpg(os.path.join(root, file), destination)

    elif input_option == 'b':

        csv_file_path = input("Enter the path to CSV file:\n(sample format: 1st col -> file_name)\n>> ")

        try:
            with open(csv_file_path, newline='', encoding='utf-8') as csv_file:
                reader = csv.reader(csv_file)

                for row in reader:
                    if row:
                        file_name = row[0].strip()
                        convert_png_to_jpg(os.path.join(source, file_name), destination)
        
        except FileNotFoundError:
            print(f"Error: CSV file not found at {csv_file_path}")
            return

    else:
        print("Invalid option. Enter 'a' or 'b'.")
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
