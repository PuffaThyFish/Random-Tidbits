from random import randrange

def printTree(size):
    # size is how many layers of tree
    print(' '*size + '*')
    
    for i in range(1, size+1):
        if i == size: # final row
            print('/' + '_'*((2*i)-1) + '\\')
            continue
        preSpaces = size-i
        midSpaces = (2*i)-1
        if i%2 == 0: # even row so straight
            toPrint = ' '*preSpaces + '|'
            for j in range(midSpaces):
                chance = randrange(0, 4)
                c = '@' if chance == 1 else ' '
                toPrint += c
            toPrint += '|'
            print(toPrint)
        else:
            toPrint = ' '*preSpaces + '/'
            for j in range(midSpaces):
                chance = randrange(0, 7)
                c = '@' if chance == 1 else ' '
                toPrint += c
            toPrint += '\\'
            print(toPrint)
    
    for i in range((size//6)+1):
        print(' '*(size-1) + '|_|')
        
def addOrnaments():
    pass

printTree(15)
