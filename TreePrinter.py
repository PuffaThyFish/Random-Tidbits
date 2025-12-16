from random import randrange

def printTree(size):
    # size is how many layers of tree
    print(' '*size + '*')
    for i in range(1, size+1):
        # add ornaments
        if randrange(0,4) == 2:
            c = '@'
        else: c = '0'
        print(' '*(size-i) + c*(1+2*i))
    
    for i in range((size//6)+1):
        print(' '*(size-1) + '|_|')

printTree(20)
