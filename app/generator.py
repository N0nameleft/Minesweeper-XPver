import random
import numpy as np

def gameMap(width, height,numMine):
    mine = minePos(width, height,numMine)
    mp = np.zeros((height,width))
    for i in range(height):
        for j in range(width):
            count = 9
            if mine[i][j] != 1:
                if i == 0:
                    if j == 0:
                        count = countMine(mine, i, j, 1)
                    elif j == width-1:
                        count = countMine(mine, i, j, 2)
                    else:
                        count = countMine(mine, i, j, 3)
                elif i == height-1:
                    if j == 0:
                        count = countMine(mine, i, j, 4)
                    elif j == width-1:
                        count = countMine(mine, i, j, 5)
                    else:
                        count = countMine(mine, i, j, 6)
                elif j == 0:
                    count = countMine(mine, i, j, 7)
                elif j == width-1:
                    count = countMine(mine, i, j, 8)
                else:
                    count = countMine(mine, i, j)

            mp[i][j] = count
    return mp
                

def countMine(mine, i, j, case=0):
    count = 0
    coors = []
    if case == 1:
        coors.extend([[i,j+1],[i+1,j],[i+1,j+1]])
    elif case == 2:
        coors.extend([[i,j-1],[i+1,j-1],[i+1,j]])
    elif case == 3:
        coors.extend([[i,j-1],[i+1,j-1],[i+1,j],[i, j+1],[i+1, j+1]])
    elif case == 4:
        coors.extend([[i-1,j],[i-1,j+1],[i,j+1]])
    elif case == 5:
        coors.extend([[i-1,j-1],[i-1,j],[i,j-1]])
    elif case == 6:
        coors.extend([[i,j-1],[i-1,j-1],[i-1,j],[i-1,j+1],[i,j+1]])
    elif case == 7:
        coors.extend([[i-1,j],[i-1,j+1],[i,j+1],[i+1,j+1],[i+1,j]])
    elif case == 8:
        coors.extend([[i-1,j],[i-1,j-1],[i,j-1],[i+1,j-1],[i+1,j]])
    else:
        for x in range(3):
            if x == 0:
                a = i-1
            elif x == 1:
                a = i
            else:
                a = i+1

            for y in range(3):
                if y == 0:
                    b = j-1
                elif y == 1:
                    b = j
                else:
                    b = j+1
                coors.append([a,b])
    
    for c in coors:
        if mine[c[0]][c[1]] == 1:
            count += 1
    return count

def minePos(width, height,numMine):
    mp = np.zeros((height,width))
    coors = []
    while len(coors) != numMine:
        x = random.randrange(width)
        y = random.randrange(height)
        if [y,x] not in coors:
            coors.append([y,x])
    
    for i in coors:
        mp[i[0]][i[1]]=1
    return mp



