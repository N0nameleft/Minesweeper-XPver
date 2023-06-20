import random
import numpy as np

def gameMap(width, height,numMine):
    mine = minePos(width, height,numMine)
    mp = np.zeros((height,width))
    for i in range(height):
        for j in range(width):
            if i == 0:
                if j == 0:
                    countMine(mine, i, j, 1)
                elif j == width-1:
                    countMine(mine, i, j, 2)
                else:
                    countMine(mine, i, j, 3)
            elif i == height-1:
                if j == 0:
                    countMine(mine, i, j, 4)
                elif j == width-1:
                    countMine(mine, i, j, 5)
                else:
                    countMine(mine, i, j, 6)
            elif j == 0:
                countMine(mine, i, j, 7)
            elif j == width-1:
                countMine(mine, i, j, 8)
            else:
                countMine(mine, i, j)

def countMine(mine, i, j, case=0):
    count = 0
    for x in range(3):
        if x == 0:
            a = i-1
        elif x == 1:
            a = i
        else:
            a = i+1

        for y in range(3):
            if x == 0:
                b = j-1
            elif x == 1:
                b = j
            else:
                b = j+1
            
            if mine[a][b] == 1:
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



print(minePos(15,10,20))


