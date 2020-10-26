import re
import sys
import time
import os

DEBUG = False

def getTimeTuple(totalTime):
    s, m, h = totalTime % 60, (totalTime // 60) % 60, (totalTime // 60 // 60)
    if DEBUG:
        print("total time: ", totalTime)
        s, m, h = totalTime % 60, (totalTime // 60) % 60, (totalTime // 60 // 60)
        print("Formatted Total Time: ", (h, m, s))

    return (h, m, s)

def getPrintString(totalTime):
    h, m, s = getTimeTuple(totalTime)
    result = []
    if h > 0: 
        result.append(h)
    if m > 0: 
      result.append(m)
    elif h > 0:
      result.append('00')
    if s >= 0:
      result.append(s)
    elif m > 0 or h > 0:
      result.append('00')

    return " : ".join(map(lambda x: str(x).rjust(2, '0'), result))

def printIt(printString):
    if not DEBUG:
        os.system("clear")
    sys.stdout.flush()
    os.system('tput cup $(( $(( $(tput lines)/2 )) - 3 ))')
    os.system(f'echo -e {printString} | figlet -tc -f Doom | lolcat -t ')
