from PIL import Image # pip install pillow
import os
import csv

def resize_images():

    # Create a dictionary to store the images to be resized
    images_to_be_resized = {}

    input_option = input("How would you like to input image names?\n(a) Manually enter the names\n(b) Paste multiple image names\n(c) Import from a CSV file\n\n>>>")

    # If manual input option is chosen
    if input_option == 'a':
        print("Enter the image names: ")

        while True:
            current_name = input("Enter the current image name:\n>>")
            if not current_name:
                break
            else:
                new_size = input(f"Enter the new size: (width height)\n>>")
                width, height = map(int, new_size.split()) # Map to store the new height and width
                images_to_be_resized[current_name] = (width, height) 

    # If paste multiple items option is chosen
    elif input_option == 'b':
        print("Paste the image names and sizes: (format -> file_name new_width new_height) ")

        while True:
            line = input(">> ")
            if not line:
                break
            else:
                parts = line.split()
                current_name = parts[0]
                size = tuple(map(int, parts[1:])) # Create a tuple
                images_to_be_resized[current_name] = size
    
    # If import from CSV file is chosen
    elif input_option == 'c':
        csv_file_path = input("Enter path to CSV file containing new image sizes:\n>>")

        try:
            with open(csv_file_path, newline='', encoding='utf-8') as csv_file:
                reader = csv.reader(csv_file)
                images_to_be_resized = {row[0].strip(): tuple(map(int, filter(None, row[1:]))) for row in reader if row}

        except FileNotFoundError:
            print(f"Error: CSV File not found at {csv_file_path}")
            return

    else:
        print("Invalid option. Enter 'a', 'b', or 'c'.")
        return

    # Enter the source path
    source = input("Enter Source:\n>>")
    
    # Iterate through the source folders
    for root, dirs, files in os.walk(source):
        for file in files:
            if file in images_to_be_resized:
                old_file_path = os.path.join(root, file)
                new_size = images_to_be_resized[file]

                try: 
                    image = Image.open(old_file_path)

                    resized_image = image.resize(new_size) # Setup the new size

                    resized_file_path = os.path.join(root, f"resized_{file}") 
                    resized_image.save(resized_file_path) # Save the resized image

                    print(f"Resized: {old_file_path} ----> {resized_file_path}")
                
                except Exception as e:
                    print(f"Error: {e}")