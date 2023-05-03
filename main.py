import sys
import time
from   lib        import graphics, tileInteractions, gameProgressHost
from   lib.data   import status
from   lib.gridRelated import graphic, system
from   lib.system import tools

ti, grps, gph = tileInteractions, graphics, gameProgressHost
s = status
grp, syst = graphic, system
tl = tools

# Game functions

sys.setrecursionlimit(10**6)
grps.intro()
s.My, s.Mx, s.mineSize = gph.init()

s.grid, s.tileGrid = syst.makeGrid(y=s.My, x=s.Mx, mineSize=s.mineSize), syst.makeTileGrid(y=s.My, x=s.Mx)
start = time.time()

while True:
    tl.clear()
    print(grp.returnGridGraphic(s.tileGrid))
    Input = input("\n위치를 입력해주세요(y x command) : ")
    commandLine = Input.split(' ')

    try:
        if int(commandLine[0]) < 0 or int(commandLine[1]) < 0 or\
           int(commandLine[0]) > len(s.grid) or int(commandLine[1]) > len(s.grid[int(commandLine[0])]): continue
    except: continue
    if len(commandLine) < 3 or len(commandLine) > 3: continue
    
    Cy, Cx = int(commandLine[0]), int(commandLine[1])
    s.y, s.x = Cy, Cx
    if commandLine[-1] == "dig":
        if s.grid[Cy][Cx] == s.icons["mine"] and s.tileGrid[Cy][Cx] == '■': gph.killGame(); break

        if s.tileGrid[Cy][Cx] != s.icons["flag"]: ti.openTile(Cy, Cx)
        if s.isMineExploded == True: gph.killGame(); break

    elif commandLine[-1] == "flag": ti.flagTile(Cy, Cx)
    
    if gph.killGame(1) == True: break

end = time.time()

explodePos = f"터진 지뢰 위치 :  y : {s.colorKey[3]}{s.y}{s.colorKey['end']}, x : {s.colorKey[3]}{s.x}{s.colorKey['end']}\n\n" if s.totalMineFound != s.mineSize else ""

print(f"""
\n
{explodePos}걸린 시간 :      {s.colorKey[2]}{end - start:.2f}{s.colorKey['end']} 초
칸 크기 :        {s.colorKey[2]}{s.My} {s.colorKey['end']}x {s.colorKey[2]}{s.Mx}{s.colorKey['end']} ({s.My*s.Mx}칸)
지뢰 밀도 :      {s.colorKey[2]}{syst.calculateDensity(s.grid)}%{s.colorKey['end']}
찾은 지뢰 개수 : {s.colorKey[2]}{s.mineSize}{s.colorKey['end']} 개 중 {s.colorKey[2] if s.totalMineFound == s.mineSize else s.colorKey[3]}{s.totalMineFound}{s.colorKey['end']} 개""")

