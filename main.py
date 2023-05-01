import random
import os
import sys
import re
import time

colorKey = {
    1     : "\033[34m",
    2     : "\033[32m",
    3     : "\033[31m",
    4     : "\033[35m",
    5     : "\033[33m",
    6     : "\033[36m",
    7     : "\033[90m",
    8     : "\033[94m",
    'end' : "\033[0m"
}

icons = {
    "mine"     : f"{colorKey[3]}*{colorKey['end']}",
    "flag"     : f"{colorKey[3]}■{colorKey['end']}",
    "notMine"  : f"{colorKey[3]}X{colorKey['end']}",
    "exploded" : f"{colorKey[3]}#{colorKey['end']}"
}
TITLE = " /|,/._  _    _    _  _  _  _  _\n/  /// //_' _\|/|//_'/_'/_//_'/ \n                       /   "

# System values
isMineExploded = False

# System functions
def clear(): os.system('clear' if os.name == 'posix' else 'cls')

def inp(string, maxInputSize:int='infinite'):
    print(string, end='')
    Input = sys.stdin.readline() if maxInputSize == 'infinite' else sys.stdin.readline(maxInputSize)
    return Input[:-1] if Input.endswith('\n') else Input

def escapeAnsi(line):
    ansi_escape =re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    return ansi_escape.sub('', line)

# Game functions
def setNumber(y, x, lu, u, ru, l, r, ld, d, rd, grid):
    posS = [lu, u, ru, l, r, ld, d, rd]
    aroundMineSize = 0
    for pos in posS:
        if grid[y+pos[0]][x+pos[1]] == icons["mine"]: aroundMineSize += 1

    return f"{colorKey[aroundMineSize]}{aroundMineSize}\033[0m" if aroundMineSize > 0 else '.'

def makeGrid(y:int, x:int, mineSize:int) -> list:
    if y*x < mineSize: raise Exception("너무 커욧")

    grid = []
    for row in range(y):
        grid.append([])
        for column in range(x): grid[row].append('.')

    count = 0
    while count < mineSize:
        Ry, Rx = random.randrange(0, y), random.randrange(0, x)
        if grid[Ry][Rx] == '.':   grid[Ry][Rx] = icons["mine"]; count += 1
        elif grid[Ry][Rx] == icons["mine"]: continue

    for row in range(y):
        for column in range(x):
            if grid[row][column] != icons["mine"]:
                posS = [
                             [-1, -1], [-1, 0], [-1, 1],
                             [0, -1],           [0, 1],
                             [1, -1],  [1, 0],  [1, 1]
                            ]
                
                if row == 0:
                    posS[0], posS[1], posS[2] = [0, 0], [0, 0], [0, 0]

                    if column == 0:                posS[3], posS[5] = [0, 0], [0, 0]
                    if column == len(grid[row])-1: posS[4], posS[7] = [0, 0], [0, 0]

                elif row == len(grid)-1:
                    posS[5], posS[6], posS[7] = [0, 0], [0, 0], [0, 0]

                    if column == 0:                posS[0], posS[3] = [0, 0], [0, 0]
                    if column == len(grid[row])-1: posS[2], posS[4] = [0, 0], [0, 0]

                elif column == 0: posS[0], posS[3], posS[5] = [0, 0], [0, 0], [0, 0]

                elif column == len(grid[row])-1: posS[2], posS[4], posS[7] = [0, 0], [0, 0], [0, 0]

                grid[row][column] = setNumber(row, column,
                                              posS[0], posS[1], posS[2], posS[3], posS[4], posS[5], posS[6], posS[7],
                                              grid)

    return grid

def makeTileGrid(y:int, x:int) -> list:
    grid = []
    for row in range(y):
        grid.append([])
        for column in range(x): grid[row].append('■')

    return grid


def calculateDensity(grid):
    fullCount, mineCount = 0, 0
    density              = 0

    for line in grid:
        for tile in line:
            fullCount += 1
            if tile == icons["mine"]: mineCount += 1

    density = (mineCount/fullCount)*100
    return int(density)

def returnGridGraphic(grid):
    def returnSquare(count) -> int:
        output = 1
        for i in range(count+1): output *= 1 if i == 0 else 10
        return output
    
    Display = ""
    maxBlankSize = len(str(len(grid)))+1

    # numberLine_X
    xNum = ""
    MAL  = len(max(grid)) # Max Array Len

    for nums in range(len(str(MAL)), -1, -1):
        startTo  = 0
        plusTo   = 1 if MAL%returnSquare(nums) != 0 else 0
        blank    = ' '*(returnSquare(nums)*2) if nums != 0 else ''

        xNum    += (f"{colorKey[3]}%{colorKey['end']}" + ' '*(maxBlankSize-1)) if nums == 0 else (" " + ' '*(maxBlankSize-1))

        if nums == 0: blank = ' '
        else:
            xNum   += blank
            blank   = ' '*((returnSquare(nums)*2)-1)
            startTo = 1

        for array in range(startTo, int(MAL/returnSquare(nums))+plusTo, 1): xNum += str(array)[-1] + blank
        xNum += "\n"

    Display += xNum

    for num, line in enumerate(grid):
        ln = (str(num) + ' '*(maxBlankSize - len(str(num))))
        Display += ln + ' '.join(line) + "\n"
    return Display

def openTile(y, x, grid, tileGrid):
    global isMineExploded

    isDigAround = False if tileGrid[y][x] == '■' else True
    tileGrid[y][x] = grid[y][x]
    mineLen        = 0

    for r1 in range(y-1, y+2):
        for c1 in range(x-1, x+2):
            if r1 < 0 or r1 > len(grid)-1 or c1 < 0 or c1 > len(grid[r1])-1: continue

            if tileGrid[r1][c1] == icons["flag"]: mineLen += 1

    for row in range(y-1, y+2):
        for column in range(x-1, x+2):
            if row < 0 or row > len(grid)-1 or column < 0 or column > len(grid[row])-1: continue

            if isDigAround and grid[y][x] not in ['.', icons["mine"], icons["exploded"]] and int(escapeAnsi(tileGrid[y][x])) == mineLen:
                if tileGrid[row][column] == '■':
                    if grid[row][column] == icons["mine"]:
                        grid[row][column] = icons["exploded"]
                        isMineExploded = True
                    elif grid[row][column] == '.': openTile(row, column, grid, tileGrid)
                    else:
                        tileGrid[row][column] = grid[row][column]
                        continue

            if grid[row][column] == icons["mine"] or tileGrid[row][column] != '■': continue

            if grid[y][x] != '.':
                if grid[row][column] != '.': continue

            if isDigAround == False: openTile(row, column, grid, tileGrid)

def checkAllTiles(end=0) -> int:
    global grid, tileGrid
    global mineSize

    if end == 0:
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if tileGrid[row][column] == icons["flag"] and grid[row][column] != icons["mine"]:
                    grid[row][column] = icons["notMine"]
        return 0
    
    elif end == 1:
        correct   = 0
        TileCount = 0
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if tileGrid[row][column] in ['■', icons["flag"]] and grid[row][column] == icons["mine"]: TileCount += 1
                if tileGrid[row][column] == icons["flag"] and grid[row][column] == icons["mine"]:
                    correct += 1

        return 1 if correct == mineSize or TileCount == mineSize else 2

def killGame(Type=0):
    global grid

    clear()
    if isMineExploded == False and Type == 0: grid[Cy][Cx] = icons["exploded"]

    finish = checkAllTiles(Type)

    if finish != 2: print(returnGridGraphic(grid))
    match finish:
        case 0: print(f"\n저런...")
        case 1: print(f"\n어케함?"); return True

def intro():
    clear()
    input(f"\n\n\n\n\n{colorKey[3]}{TITLE}{colorKey['end']}\n\n          PRESS ENTER")

def init():
    global y, x, mineSize

    def question(text:str, Type:str=None):
        while True:
            clear()
            Input = input(text)
            try:
                if Type != "mine" and int(Input) <= 1: continue
                if Type == "mine":
                    if int(Input) >= y*x: continue
            except: continue
            else: break
        return int(Input)
    
    y        = question("y값을 입력해주세요 : ")
    x        = question("x값을 입력해주세요 : ")
    mineSize = question(f"지뢰의 개수를 정해주세요({y*x}개 보다 같거나 크면 안됩니다!) : ", "mine")


sys.setrecursionlimit(10**6)
intro()
init()

grid, tileGrid = makeGrid(y=y, x=x, mineSize=mineSize), makeTileGrid(y=y, x=x)

while True:
    clear()
    print(returnGridGraphic(tileGrid))
    Input = input("\n위치를 입력해주세요(y x command) : ")
    commandLine = Input.split(' ')

    try:
        if int(commandLine[0]) < 0 or int(commandLine[1]) < 0 or\
           int(commandLine[0]) > len(grid) or int(commandLine[1]) > len(grid[int(commandLine[0])]): continue
    except: continue
    if len(commandLine) < 3 or len(commandLine) > 3: continue
    
    Cy, Cx = int(commandLine[0]), int(commandLine[1])
    if commandLine[-1] == "dig":
        if grid[Cy][Cx] == icons["mine"] and tileGrid[Cy][Cx] == '■': killGame(); break

        openTile(y=Cy, x=Cx, grid=grid, tileGrid=tileGrid)
        if isMineExploded == True: killGame(); break

    elif commandLine[-1] == "flag":
        target = tileGrid[Cy][Cx]
        if   target == icons["flag"]: tileGrid[Cy][Cx] = '■'
        elif target == '■': tileGrid[Cy][Cx] = icons["flag"]
    
    if killGame(1) == True: break
