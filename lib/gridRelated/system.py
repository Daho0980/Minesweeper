import random
from   lib.data import status as s

def setNumber(y, x, lu, u, ru, l, r, ld, d, rd, grid):
    mineCount = 0
    
    for pos in [lu, u, ru, l, r, ld, d, rd]:
        if grid[y+pos[0]][x+pos[1]] == s.icons["mine"]: mineCount += 1

    return f"{s.colorKey[mineCount]}{mineCount}\033[0m" if mineCount > 0 else '.'

def peripheralSensing(y, x, grid):

    posS = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1],           [0, 1],
        [1, -1],  [1, 0],  [1, 1]
        ]
                
    if y == 0:
        posS[0], posS[1], posS[2] = [0, 0], [0, 0], [0, 0]

        if x == 0:                posS[3], posS[5] = [0, 0], [0, 0]
        if x == len(grid[y])-1: posS[4], posS[7] = [0, 0], [0, 0]

    elif y == len(grid)-1:
        posS[5], posS[6], posS[7] = [0, 0], [0, 0], [0, 0]

        if x == 0:                posS[0], posS[3] = [0, 0], [0, 0]
        if x == len(grid[y])-1: posS[2], posS[4] = [0, 0], [0, 0]

    elif x == 0: posS[0], posS[3], posS[5] = [0, 0], [0, 0], [0, 0]

    elif x == len(grid[y])-1: posS[2], posS[4], posS[7] = [0, 0], [0, 0], [0, 0]

    return posS

def selectGridType(grid:list, Type:int):
    output = []

    for row in range(len(grid)):
        output.append([])
        for column in range(len(grid[row])):
            output[row].append(grid[row][column][Type])

    return output

def createGrid(y:int, x:int, mineSize:int) -> list:
    if y*x < mineSize: raise Exception("이스터에그를 찾으셨네요 짞짞짞")

    grid = []
    for row in range(y):
        grid.append([])
        for column in range(x): grid[row].append(['.', '■'])

    count = 0
    while count < mineSize:
        Ry, Rx = random.randrange(0, y), random.randrange(0, x)
        if grid[Ry][Rx][0] == '.': grid[Ry][Rx][0] = s.icons["mine"]; count += 1
        elif grid[Ry][Rx][0] == s.icons["mine"]: continue

    for row in range(y):
        for column in range(x):
            if grid[row][column][0] != s.icons["mine"]:
                posS = peripheralSensing(row, column, grid)

                grid[row][column][0] = setNumber(row, column,
                                                 posS[0], posS[1], posS[2], posS[3], posS[4], posS[5], posS[6], posS[7],
                                                 selectGridType(grid=grid, Type=0))
                
    return grid

def calculateDensity(grid):
    fullCount, mineCount = 0, 0
    density              = 0

    for line in grid:
        for tile in line:
            fullCount += 1
            if tile == s.icons["mine"]: mineCount += 1

    density = (mineCount/fullCount)*100
    return int(density)

def checkAllTiles(end=0) -> int:
    def checkUnderFlag():
        count = 0
        for row in range(len(s.mg)):
            for column in range(len(s.mg[row])):
                if s.mg[row][column][1] == s.icons["flag"] and s.mg[row][column][0] == s.icons["mine"]:
                    count += 1
        return count

    s.totalMineFound = checkUnderFlag()

    if end == 0:
        for row in range(len(s.mg)):
            for column in range(len(s.mg[row])):
                if s.mg[row][column][1] == s.icons["flag"] and s.mg[row][column][0] != s.icons["mine"]:
                    s.mg[row][column][0] = s.icons["notMine"]
        return 0
    
    elif end == 1:
        correct   = 0
        TileCount = 0
        for row in range(len(s.mg)):
            for column in range(len(s.mg[row])):
                if s.mg[row][column][1] in ['■', s.icons["flag"]]: TileCount += 1
                if s.mg[row][column][1] == s.icons["flag"] and s.mg[row][column][0] == s.icons["mine"]:
                    correct += 1
        if TileCount == s.mineSize: s.totalMineFound = s.mineSize

        return 1 if correct == s.mineSize or TileCount == s.mineSize else 2