from lib.data        import status as s
from lib.gridRelated import system as syst
from lib.system      import tools  as tl

def openTile(y:int, x:int):
    isDigAround      = False if s.mg[y][x][1] == '■' else True
    s.mg[y][x][1] = s.mg[y][x][0]
    mineLen          = 0

    for r1 in range(y-1, y+2):
        for c1 in range(x-1, x+2):
            if r1 < 0 or r1 > len(s.mg)-1 or c1 < 0 or c1 > len(s.mg[r1])-1: continue

            if s.mg[r1][c1][1] == s.icons["flag"]: mineLen += 1

    for row in range(y-1, y+2):
        for column in range(x-1, x+2):
            if row < 0 or row > len(s.mg)-1 or column < 0 or column > len(s.mg[row])-1: continue

            if isDigAround and s.mg[y][x][0] not in ['.', s.icons["mine"], s.icons["exploded"]] and int(tl.escapeAnsi(s.mg[y][x][1])) == mineLen:
                if s.mg[row][column][1] == '■':
                    if s.mg[row][column][0] == s.icons["mine"]:
                        s.mg[row][column][0] = s.icons["exploded"]
                        s.isMineExploded    = True

                    elif s.mg[row][column][0] == '.': openTile(row, column)

                    else:
                        s.mg[row][column][1] = s.mg[row][column][0]
                        continue

            if s.mg[row][column][0] == s.icons["mine"] or s.mg[row][column][1] != '■': continue

            if s.mg[y][x][0] != '.':
                if s.mg[row][column][0] != '.': continue

            if isDigAround == False: openTile(row, column)

def flagTile(y, x):
    target = s.mg[y][x][1]
    
    if   target == '■':          s.mg[y][x][1] = s.icons["flag"]
    elif target == s.icons["flag"]: s.mg[y][x][1] = '■'
    else:
        posS         = syst.peripheralSensing(y, x, syst.selectGridType(grid=s.mg, Type=0))
        unDIggedTile = 0

        for i in posS:
            if s.mg[y+i[0]][x+i[1]][1] in [s.icons["flag"], '■']: unDIggedTile += 1

        if int(tl.escapeAnsi(s.mg[y][x][1])) == unDIggedTile:
            for i in posS:
                target = s.mg[y+i[0]][x+i[1]][1]

                if target == '■': s.mg[y+i[0]][x+i[1]][1] = s.icons["flag"]