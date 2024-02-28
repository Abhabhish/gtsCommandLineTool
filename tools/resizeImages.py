from PIL import Image
import os
import csv

def resize_images():
    images_to_be_resized = {}

    input_option = input("How would you like to input image file names?\n(a) Manually enter the file names\n(b) Paste multiple image file names\n(c) Import from a CSV file\n\n>>>")

    if input_option == 'a':
        print("Enter the image file names: ")
        
        while True:
            current_name = input("Enter the current image name:\n>>")

            if not current_name:
                break
            else:
                width = int(input("Enter the new width:\n>>"))
                images_to_be_resized[current_name] = (width, 0)

    elif input_option == 'b':
        print("Paste the image file names: (format -> file_name new_width)")

        while True:
            line = input(">> ")

            if not line:
                break
            else:
                parts = line.split()
                current_name = parts[0]
                width = int(parts[1])
                images_to_be_resized[current_name] = (width, 0)

    elif input_option == 'c':
        csv_file_path = input("Enter the path to the CSV file:\n>>")

        try:
            with open(csv_file_path, newline='', encoding='utf-8') as csv_file:
                reader = csv.reader(csv_file)
                
                for row in reader:
                    current_name = row[0].strip()
                    width = int(row[1])
                    images_to_be_resized[current_name] = (width, 0)

        except FileNotFoundError:
            print(f"Error: CSV file not found at {csv_file_path}")
            return
    
    else:
        print("Invalid option. Enter 'a', 'b' or 'c'.")
        return

    source = input("Enter the source:\n>>")

    for root, dirs, files in os.walk(source):
        for file in files:
            if file in images_to_be_resized:
                old_file_path = os.path.join(root, file)
                new_size = images_to_be_resized[file]

                try:
                    image = Image.open(old_file_path)
                    aspect_ratio = image.width / new_size[0]

                    new_height = int(image.height / aspect_ratio)
                    new_size = (new_size[0], new_height)

                    resized_image = image.resize(new_size)
                    resized_file_path = os.path.join(root, f"resized_{file}")

                    resized_image.save(resized_file_path)

                    print(f"Resized: {old_file_path} ----> {resized_file_path}")
                
                except Exception as e:
                    print("Error: {e}")
