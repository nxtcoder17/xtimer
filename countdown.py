import time
import sys
import re
import os

from libs import getPrintString, printIt

DEBUG = False

userTime = sys.argv[1]

REGEX_PATTERN = r"(([0-9]{,2})h)?(([0-9]{,2})m)?(([0-9]{,2})s)?"

if DEBUG:
    print("Matches:", re.match(REGEX_PATTERN, userTime).groups())
matches = re.match(REGEX_PATTERN, userTime).groups()

h, m, s = [0 if matches[x] is None else int(matches[x]) for x in range(1, len(matches), 2)]

totalTime = h * 60 * 60 + m * 60 + s

while totalTime >= 0:
    printIt(getPrintString(totalTime))
    time.sleep(1)
    totalTime -= 1
os.system("clear")
