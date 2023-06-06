from lib.data import status as s

def returnGridGraphic(grid):
    def returnSquare(count) -> int:
        output = 1
        for i in range(count+1): output *= 1 if i == 0 else 10
        return output
    
    Display      = ""
    maxBlankSize = len(str(len(grid)-1))+1

    lineX = ""
    MAL  = len(max(grid)) # Max number's length

    for nums in range(len(str(MAL)), -1, -1): # Print stacked X-coordinate
        startTo   = 0
        plusTo    = 1 if MAL%returnSquare(nums) != 0 else 0
        blank     = ' '*(returnSquare(nums)*2) if nums != 0 else ''

        lineX    += (f"{s.colorKey[3]}%{s.colorKey['end']}" + ' '*(maxBlankSize-1)) if nums == 0 else (" " + ' '*(maxBlankSize-1))

        if nums == 0: blank = ' '
        else:
            lineX   += blank
            blank   = ' '*((returnSquare(nums)*2)-1)
            startTo = 1

        for array in range(startTo, int(MAL/returnSquare(nums))+plusTo, 1):
            highlight = s.bgcolorKey[3] if array == int(s.x/returnSquare(nums)) else ""
            lineX += highlight + str(array)[-1] + "\033[0m" + blank
        lineX += "\n"

    Display += lineX

    for num, line in enumerate(grid): # Print Y-coordinate and grid
        highlight = s.bgcolorKey[3] if num == s.y else ""
        ln        = highlight + str(num) + "\033[0m" + ' '*(maxBlankSize - len(str(num)))
        Display  += ln + ' '.join(line) + "\n"
        
    return Display