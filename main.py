import sys
import time
from   lib             import graphics, tileInteractions, gameProgressHost
from   lib.data        import globalVars
from   lib.gridRelated import graphic, system
from   lib.system      import tools

ti, grps, gph = tileInteractions, graphics, gameProgressHost
s             = globalVars
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
    Input = input(f"\n위치를 입력해주세요(y x command) : {s.colorKey[2]}"); print(s.colorKey['end'], end='')
    commandLine = Input.split(' ')

    limits = [[-len(s.mg), -len(s.mg[0])], [len(s.mg), len(s.mg[0])]]
    for step, coordinate in enumerate(commandLine[:-2]):
        escape = False
        Type = None

        try:    int(coordinate)+1; Type = 1
        except: Type = 0

        match Type:
            case 0:
                if coordinate != s.settings["CMK"]: escape = True; break
            case 1:
                if int(coordinate) < limits[0][step] or int(coordinate) >= limits[1][step]: escape = True; break
    if escape == True: continue

    if len(commandLine) < 3 or len(commandLine) > 3: continue
    
    Cy = s.y if commandLine[0] == s.settings["CMK"] else int(commandLine[0]) if int(commandLine[0]) >= 0 else (len(s.mg)+int(commandLine[0]))
    Cx = s.x if commandLine[1] == s.settings["CMK"] else int(commandLine[1]) if int(commandLine[1]) >= 0 else (len(s.mg[int(commandLine[0])])+int(commandLine[1]))
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
지뢰 밀도 :      {grps.checkDensity(syst.calculateDensity(syst.selectGridType(grid=s.mg, Type=0)))} ({s.mineSize}개)
찾은 지뢰 개수 : {s.colorKey[2]}{s.mineSize}{s.colorKey['end']} 개 중 {s.colorKey[2] if s.totalMineFound == s.mineSize else s.colorKey[3]}{s.totalMineFound}{s.colorKey['end']} 개""")

