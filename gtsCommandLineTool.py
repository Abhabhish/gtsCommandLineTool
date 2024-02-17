from tools.copyfiles import copy
from tools.moveFiles import move


def asking_query():
    global Operation
    Query = input('What do you want to do? \n(a)copy\n(b)move\n\n>>>')
    if Query == 'a':
        copy()
    elif Query == 'b':
        move()
    else:
        print('sorry, I can not understand')
        asking_query()
asking_query()
