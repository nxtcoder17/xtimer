#! /usr/bin/python
import time

from libs import getPrintString, printIt

allowedInterrupt = 1
totalTime = 0
while True:
    try:
        printIt(getPrintString(totalTime))
        time.sleep(1)
        totalTime += 1
    except KeyboardInterrupt:
        printIt("Stopwatch Paused ...")
        x = input()
        if x:
            continue

