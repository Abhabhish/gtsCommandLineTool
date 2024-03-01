from tools.copyFiles import copy # Copy functionality
from tools.moveFiles import move # Move functionality
from tools.copyWithSegregation import copy_with_segregation # Copy with segregation functionality
from tools.moveWithSegregation import move_with_segregation # Move with segregation functionality
from tools.deleteFiles import delete # Delete functionality
from tools.renameFiles import rename # Rename functionality
from tools.resizeImages import resize_images # Resize functionality
from tools.removeNoise import remove_noise # Noise removal functionality
from tools.downloadFiles import download_files # Download functionality
from tools.pngTojpg import png_to_jpg # PNG to JPG functionality
from tools.heicTojpg import heic_to_jpg # HEIC to JPG functionality
from tools.combineCsv import combine_csv_files # Combine CSV functionality

# Function to give options to the user for functionality
def asking_query(): 
    
    global Operation

    # Option input
    Query = input('What do you want to do? \n(a) Copy\n(b) Move\n(c) Copy with segregation\n(d) Move with segregation\n(e) Delete\n(f) Rename\n(g) Resize Image\n(h) Remove Noise\n(i) Download Files\n(j) PNG to JPG\n(k) HEIC to JPG\n(l) Combine CSV files\n\n>>>')

    # Match statement for options
    match Query:
        case 'a': copy()
        case 'b': move()
        case 'c': copy_with_segregation()
        case 'd': move_with_segregation()
        case 'e': delete()
        case 'f': rename()
        case 'g': resize_images()
        case 'h': remove_noise()
        case 'i': download_files()
        case 'j': png_to_jpg()
        case 'k': heic_to_jpg()
        case 'l': combine_csv_files()
        case _:
            # Ask again if none of the options above are chosen
            print('Please choose one of the options given above only.')
            asking_query()

asking_query()
