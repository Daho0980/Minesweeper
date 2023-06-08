from lib.data        import globalVars          as s
from lib.gridRelated import graphic, system
from lib.system      import tools           as tl

grp, syst = graphic, system

def init():

    def question(text:str, Type:str=None, opy:int=None, opx:int=None) -> int:
        while True:
            tl.clear()
            Input = input(text)
            try:
                if Type != "mine" and int(Input) <= 1: continue
                if Type == "mine":
                    if int(Input) >= opy*opx: continue
            except: continue
            else: break
        return int(Input)
    
    outputY  = question("y값을 입력해주세요 : ")
    outputX  = question("x값을 입력해주세요 : ")
    outputMS = question(f"지뢰의 개수를 정해주세요({outputY*outputX}개 보다 같거나 크면 안됩니다!) : ", Type="mine", opy=outputY, opx=outputX)

    return outputY, outputX, outputMS

def killGame(Type=0, Cy=0, Cx=0):
    tl.clear()
    if s.isMineExploded == False and Type == 0 and s.mg[Cy][Cx][0] == s.icons["mine"]: s.mg[Cy][Cx][0] = s.icons["exploded"]

    finish = syst.checkAllTiles(Type)

    if finish != 2: print(grp.returnGridGraphic(syst.selectGridType(grid=s.mg, Type=0)))
    match finish:
        case 0: print(f"\n저런...")
        case 1: print(f"\n어케함?"); return True