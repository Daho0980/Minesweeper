from lib.data import status as s
from lib.system import tools as tl

def intro():
    tl.clear()
    input(f"\n\n\n\n\n{s.colorKey[3]}{s.TITLE}{s.colorKey['end']}\n\n          PRESS ENTER")

def checkDensity(density):
    color     = s.colorKey[7]
    guideText = "우린 이런 거 취급 안합니다"

    for step in s.densityStep:
        if density >= step:
            color, guideText = s.densityStep[step][0], s.densityStep[step][1]
            if density == step: break

    return f"{color}{density}% ({guideText}){s.colorKey['end']}"