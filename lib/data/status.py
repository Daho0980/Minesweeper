# Graphics
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

# Systems
y, x           = 0, 0
totalMineFound = 0
isMineExploded = False

My       = 0
Mx       = 0
mineSize = 0

# grids
mg = []