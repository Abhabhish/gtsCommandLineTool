from tools.copyfiles import copy


def asking_query():
    global Operation
    Query = input('What do you want to do? \n(a)copy\n\n>>>')
    if Query == 'a':
        copy()
    else:
        print('sorry I can not understand')
        asking_query()
asking_query()



