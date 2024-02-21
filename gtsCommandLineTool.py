from tools.copyFiles import copy
from tools.moveFiles import move
from tools.deleteFiles import delete
from tools.renameFiles import rename
from tools.resizeImages import resize_images
from tools.removeNoise import remove_noise
from tools.downloadFiles import download_files


def asking_query():
    
    global Operation

    Query = input('What do you want to do? \n(a) Copy\n(b) Move\n(c) Copy with segregation (Yet to be implemented)\n(d) Move with segregation (Yet to be implemented)\n(e) Delete\n(f) Rename\n(g) Resize Image\n(h) Remove Noise\n(i) Download Files\n\n>>>')

    match Query:
        case 'a': copy()
        case 'b': move()
        case 'c' | 'd': return 0
        case 'e': delete()
        case 'f': rename()
        case 'g': resize_images()
        case 'h': remove_noise()
        case 'i': download_files()
        case _:
            print('sorry, I can not understand')
            asking_query()


asking_query()
