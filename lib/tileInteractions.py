from lib.data        import status as s
from lib.gridRelated import system as syst
from lib.system      import tools  as tl

def openTile(y:int, x:int):
    isDigAround      = False if s.tileGrid[y][x] == '■' else True
    s.tileGrid[y][x] = s.grid[y][x]
    mineLen          = 0

    for r1 in range(y-1, y+2):
        for c1 in range(x-1, x+2):
            if r1 < 0 or r1 > len(s.grid)-1 or c1 < 0 or c1 > len(s.grid[r1])-1: continue

            if s.tileGrid[r1][c1] == s.icons["flag"]: mineLen += 1

    for row in range(y-1, y+2):
        for column in range(x-1, x+2):
            if row < 0 or row > len(s.grid)-1 or column < 0 or column > len(s.grid[row])-1: continue

            if isDigAround and s.grid[y][x] not in ['.', s.icons["mine"], s.icons["exploded"]] and int(tl.escapeAnsi(s.tileGrid[y][x])) == mineLen:
                if s.tileGrid[row][column] == '■':
                    if s.grid[row][column] == s.icons["mine"]:
                        s.grid[row][column] = s.icons["exploded"]
                        s.isMineExploded    = True

                    elif s.grid[row][column] == '.': openTile(row, column)

                    else:
                        s.tileGrid[row][column] = s.grid[row][column]
                        continue

            if s.grid[row][column] == s.icons["mine"] or s.tileGrid[row][column] != '■': continue

            if s.grid[y][x] != '.':
                if s.grid[row][column] != '.': continue

            if isDigAround == False: openTile(row, column)

def flagTile(y, x):
    target = s.tileGrid[y][x]
    
    if   target == '■':          s.tileGrid[y][x] = s.icons["flag"]
    elif target == s.icons["flag"]: s.tileGrid[y][x] = '■'
    else:
        posS         = syst.peripheralSensing(y, x, s.grid)
        unDIggedTile = 0

        for i in posS:
            if s.tileGrid[y+i[0]][x+i[1]] in [s.icons["flag"], '■']: unDIggedTile += 1

        if int(tl.escapeAnsi(s.tileGrid[y][x])) == unDIggedTile:
            for i in posS:
                target = s.tileGrid[y+i[0]][x+i[1]]

                if target == '■': s.tileGrid[y+i[0]][x+i[1]] = s.icons["flag"]