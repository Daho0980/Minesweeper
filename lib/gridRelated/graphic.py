from lib.data import globalVars as s

def returnGridGraphic(grid):
    def returnSquare(count) -> int:
        output = 1
        for i in range(count+1): output *= 1 if i == 0 else 10
        return output
    
    maxBlankSize = len(str(len(grid)-1))+1

    def xLine(Type:int) -> str:
        """
        overLine : 0
        underLine : 1
        """
        lineX       = ""
        MAL         = len(max(grid)) # Max number's length

        direction = {
            0 : [len(str(MAL)), -1, -1],
            1 : [0, len(str(MAL))+1, 1]
        }
        corner = {
            0 : [f"{s.colorKey[3]}/{s.colorKey['end']}", f"{s.colorKey[3]}\\{s.colorKey['end']}"],
            1 : [f"{s.colorKey[3]}\\{s.colorKey['end']}", f"{s.colorKey[3]}/{s.colorKey['end']}"],
        }

        for nums in range(direction[Type][0], direction[Type][1], direction[Type][2]): # Print stacked X-coordinate
            startTo   = 0
            plusTo    = 1 if MAL%returnSquare(nums) != 0 else 0
            blank     = ' '*(returnSquare(nums)*2) if nums != 0 else ''

            lineX    += (corner[Type][0] + ' '*(maxBlankSize-1)) if nums == 0 else (" " + ' '*(maxBlankSize-1))

            if nums == 0: blank = ' '
            else:
                lineX   += blank
                blank   = ' '*((returnSquare(nums)*2)-1)
                startTo = 1

            for array in range(startTo, int(MAL/returnSquare(nums))+plusTo, 1):
                highlight = s.bgcolorKey[3] if array == int(s.x/returnSquare(nums)) else ""
                lineX += highlight + str(array)[-1] + s.colorKey['end'] + blank
            lineX += f" {corner[Type][1]}\n" if nums == 0 else "\n"
        
        return lineX

    Display  = ""
    Display += xLine(0)

    for num, line in enumerate(grid): # Print Y-coordinate and grid
        highlight = s.bgcolorKey[3] if num == s.y else ""
        ln        = highlight + str(num) + s.colorKey['end'] + ' '*(maxBlankSize - len(str(num)))
        Display  += ln + ' '.join(line) + f"  {highlight}{str(num)}{s.colorKey['end']}\n"

    Display += xLine(1)
        
    return Display