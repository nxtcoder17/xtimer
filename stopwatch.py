import time

from libs import getPrintString, printIt

totalTime = 0
while True:
    printIt(getPrintString(totalTime))
    time.sleep(1)
    totalTime += 1

