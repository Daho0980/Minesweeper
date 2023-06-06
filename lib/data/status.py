# Graphics
colorKey = {
    1     : "\033[34m", # blue
    2     : "\033[32m", # green
    3     : "\033[31m", # red
    4     : "\033[35m", # magenta
    5     : "\033[33m", # yellow
    6     : "\033[36m", # light green?
    7     : "\033[90m", # grey
    8     : "\033[94m", # light blue
    'end' : "\033[0m" # end color code
}

densityStep = {
    10  : [colorKey[8], "아주 적음"],
    20 : [colorKey[1], "적음"],
    40 : [colorKey[2], "균일함"],
    60 : [colorKey[6], "풍부함"],
    80 : [colorKey[4], "많음"],
    90 : [colorKey[3], "너무 많음"]
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