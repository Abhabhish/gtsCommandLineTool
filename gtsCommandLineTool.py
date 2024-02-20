from tools.copyFiles import copy
from tools.moveFiles import move
from tools.deleteFiles import delete
from tools.renameFiles import rename
from tools.resizeImages import resize_images
from tools.removeNoise import remove_noise


def asking_query():
    
    global Operation

    Query = input('What do you want to do? \n(a) Copy\n(b) Move\n(c) Copy with segregation (Yet to be implemented)\n(d) Move with segregation (Yet to be implemented)\n(e) Delete\n(f) Rename\n(g) Resize Image\n(h) Remove Noise\n\n>>>')

    if Query == 'a':
        copy()
    elif Query == 'b':
        move()
    elif Query == 'c':
        return 0
    elif Query == 'd':
        return 0
    elif Query == 'e':
        delete()
    elif Query == 'f':
        rename()
    elif Query == 'g':
        resize_images()
    elif Query == 'h':
        remove_noise()
    else:
        print('sorry, I can not understand')
        asking_query()


asking_query()
