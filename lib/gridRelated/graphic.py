from lib.data import status as s

def returnGridGraphic(grid):
    def returnSquare(count) -> int:
        output = 1
        for i in range(count+1): output *= 1 if i == 0 else 10
        return output
    
    Display      = ""
    maxBlankSize = len(str(len(grid)-1))+1

    # numberLine_X
    xNum = ""
    MAL  = len(max(grid)) # Max Array Len

    for nums in range(len(str(MAL)), -1, -1):
        startTo   = 0
        plusTo    = 1 if MAL%returnSquare(nums) != 0 else 0
        blank     = ' '*(returnSquare(nums)*2) if nums != 0 else ''

        xNum    += (f"{s.colorKey[3]}%{s.colorKey['end']}" + ' '*(maxBlankSize-1)) if nums == 0 else (" " + ' '*(maxBlankSize-1))

        if nums == 0: blank = ' '
        else:
            xNum   += blank
            blank   = ' '*((returnSquare(nums)*2)-1)
            startTo = 1

        for array in range(startTo, int(MAL/returnSquare(nums))+plusTo, 1):
            highlight = "\033[41m" if array == s.x and nums == 0 else ""
            xNum += highlight + str(array)[-1] + "\033[0m" + blank
        xNum += "\n"

    Display += xNum

    for num, line in enumerate(grid):
        highlight = "\033[41m" if num == s.y else ""
        ln        = highlight + str(num) + "\033[0m" + ' '*(maxBlankSize - len(str(num)))
        Display  += ln + ' '.join(line) + "\n"
        
    return Display