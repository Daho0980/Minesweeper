# colors
colorKey = {
    1     : "\033[34m", # blue
    2     : "\033[32m", # green
    3     : "\033[31m", # red
    4     : "\033[35m", # magenta
    5     : "\033[33m", # yellow
    6     : "\033[36m", # cyan
    7     : "\033[90m", # grey
    8     : "\033[94m", # bright blue
    'end' : "\033[0m" # end color code
}

bgcolorKey = {
    1 : "\033[44m",  # blue
    2 : "\033[42m",  # green
    3 : "\033[41m",  # red
    4 : "\033[45m",  # magenta
    5 : "\033[43m",  # yellow
    6 : "\033[46m",  # cyan
    7 : "\033[100m", # grey
    8 : "\033[104"   # bright blue
}

# graphic?
densityStep = {
    10  : [colorKey[8], "아주 적음"],
    20 : [colorKey[1], "적음"],
    40 : [colorKey[2], "균일함"],
    60 : [colorKey[6], "풍부함"],
    80 : [colorKey[4], "많음"],
    90 : [colorKey[3], "너무 많음"]
}

# icons
icons = {
    "mine"     : f"{bgcolorKey[3]}*{colorKey['end']}",
    "flag"     : f"{colorKey[3]}■{colorKey['end']}",
    "notMine"  : f"{bgcolorKey[3]}X{colorKey['end']}",
    "exploded" : f"{bgcolorKey[1]}#{colorKey['end']}"
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