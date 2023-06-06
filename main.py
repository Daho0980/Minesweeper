import sys
import time
from   lib             import graphics, tileInteractions, gameProgressHost
from   lib.data        import status
from   lib.gridRelated import graphic, system
from   lib.system      import tools

ti, grps, gph = tileInteractions, graphics, gameProgressHost
s             = status
grp, syst     = graphic, system
tl            = tools

# Game functions

sys.setrecursionlimit(10**6)
grps.intro()
s.My, s.Mx, s.mineSize = gph.init()
s.mg = syst.createGrid(s.My, s.Mx, s.mineSize)

start = time.time()

while True:
    tl.clear()
    print(grp.returnGridGraphic(syst.selectGridType(grid=s.mg, Type=1)))
    Input = input("\n위치를 입력해주세요(x y command) : ")
    commandLine = Input.split(' ')

    try:
        if int(commandLine[0]) < 0 or int(commandLine[1]) < 0 or\
           int(commandLine[0]) > len(s.mg) or int(commandLine[1]) > len(s.mg[int(commandLine[0])]): continue
    except: continue
    if len(commandLine) < 3 or len(commandLine) > 3: continue
    
    Cy, Cx = int(commandLine[0]), int(commandLine[1])
    s.y, s.x = Cy, Cx
    if commandLine[-1] == "dig":
        if s.mg[Cy][Cx][0] == s.icons["mine"] and s.mg[Cy][Cx][1] == '■': gph.killGame(Cy=s.y, Cx=s.x); break

        if s.mg[Cy][Cx][1] != s.icons["flag"]: ti.openTile(Cy, Cx)
        if s.isMineExploded == True: gph.killGame(Cy=s.y, Cx=s.x); break

    elif commandLine[-1] == "flag": ti.flagTile(Cy, Cx)
    
    if gph.killGame(Type=1, Cy=s.y, Cx=s.x) == True: break

end = time.time()

explodePos = f"터진 지뢰 위치 :  y : {s.colorKey[3]}{s.y}{s.colorKey['end']}, x : {s.colorKey[3]}{s.x}{s.colorKey['end']}\n\n" if s.totalMineFound != s.mineSize else ""

print(f"""
\n
{explodePos}걸린 시간 :      {s.colorKey[2]}{end - start:.2f}{s.colorKey['end']} 초
칸 크기 :        {s.colorKey[2]}{s.My} {s.colorKey['end']}x {s.colorKey[2]}{s.Mx}{s.colorKey['end']} ({s.My*s.Mx}칸)
지뢰 밀도 :      {s.colorKey[2]}{syst.calculateDensity(syst.selectGridType(grid=s.mg, Type=0))}%{s.colorKey['end']}
찾은 지뢰 개수 : {s.colorKey[2]}{s.mineSize}{s.colorKey['end']} 개 중 {s.colorKey[2] if s.totalMineFound == s.mineSize else s.colorKey[3]}{s.totalMineFound}{s.colorKey['end']} 개""")

