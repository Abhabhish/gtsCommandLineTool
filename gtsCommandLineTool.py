from tools.copyFiles import copy
from tools.moveFiles import move
from tools.deleteFiles import delete
from tools.renameFiles import rename


def asking_query():
    
    global Operation

    Query = input('What do you want to do? \n(a) Copy\n(b) Move\n(c) Copy with segregation (Yet to be implemented)\n(d) Move with segregation (Yet to be implemented)\n(e) Delete\n(f) Rename\n\n>>>')

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
    else:
        print('sorry, I can not understand')
        asking_query()


asking_query()
