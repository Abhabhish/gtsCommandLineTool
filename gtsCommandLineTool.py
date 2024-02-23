from tools.copyFiles import copy 
from tools.moveFiles import move
from tools.copyWithSegregation import copy_with_segregation
from tools.moveWithSegregation import move_with_segregation
from tools.deleteFiles import delete
from tools.renameFiles import rename
from tools.resizeImages import resize_images
from tools.removeNoise import remove_noise
from tools.downloadFiles import download_files
from tools.pngTojpg import png_to_jpg
from tools.heicTojpg import heic_to_jpg
from tools.combineCsv import combine_csv_files


def asking_query():
    
    global Operation

    Query = input('What do you want to do? \n(a) Copy\n(b) Move\n(c) Copy with segregation\n(d) Move with segregation (Yet to be implemented)\n(e) Delete\n(f) Rename\n(g) Resize Image\n(h) Remove Noise\n(i) Download Files\n(j) PNG to JPG\n(k) HEIC to JPG\n(l) Combine CSV files\n\n>>>')

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
            print('Please choose one of the options given above only.')
            asking_query()


asking_query()
