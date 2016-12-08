#!/usr/bin/env python3
import re

theInput = """rect 1x1
rotate row y=0 by 20
rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 3
rect 2x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 3
rect 2x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 4
rect 2x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 3
rect 2x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 6
rect 5x1
rotate row y=0 by 2
rect 1x3
rotate row y=2 by 8
rotate row y=0 by 8
rotate column x=0 by 1
rect 7x1
rotate row y=2 by 24
rotate row y=0 by 20
rotate column x=5 by 1
rotate column x=4 by 2
rotate column x=2 by 2
rotate column x=0 by 1
rect 7x1
rotate column x=34 by 2
rotate column x=22 by 1
rotate column x=15 by 1
rotate row y=2 by 18
rotate row y=0 by 12
rotate column x=8 by 2
rotate column x=7 by 1
rotate column x=5 by 2
rotate column x=2 by 1
rotate column x=0 by 1
rect 9x1
rotate row y=3 by 28
rotate row y=1 by 28
rotate row y=0 by 20
rotate column x=18 by 1
rotate column x=15 by 1
rotate column x=14 by 1
rotate column x=13 by 1
rotate column x=12 by 2
rotate column x=10 by 3
rotate column x=8 by 1
rotate column x=7 by 2
rotate column x=6 by 1
rotate column x=5 by 1
rotate column x=3 by 1
rotate column x=2 by 2
rotate column x=0 by 1
rect 19x1
rotate column x=34 by 2
rotate column x=24 by 1
rotate column x=23 by 1
rotate column x=14 by 1
rotate column x=9 by 2
rotate column x=4 by 2
rotate row y=3 by 5
rotate row y=2 by 3
rotate row y=1 by 7
rotate row y=0 by 5
rotate column x=0 by 2
rect 3x2
rotate column x=16 by 2
rotate row y=3 by 27
rotate row y=2 by 5
rotate row y=0 by 20
rotate column x=8 by 2
rotate column x=7 by 1
rotate column x=5 by 1
rotate column x=3 by 3
rotate column x=2 by 1
rotate column x=1 by 2
rotate column x=0 by 1
rect 9x1
rotate row y=4 by 42
rotate row y=3 by 40
rotate row y=1 by 30
rotate row y=0 by 40
rotate column x=37 by 2
rotate column x=36 by 3
rotate column x=35 by 1
rotate column x=33 by 1
rotate column x=32 by 1
rotate column x=31 by 3
rotate column x=30 by 1
rotate column x=28 by 1
rotate column x=27 by 1
rotate column x=25 by 1
rotate column x=23 by 3
rotate column x=22 by 1
rotate column x=21 by 1
rotate column x=20 by 1
rotate column x=18 by 1
rotate column x=17 by 1
rotate column x=16 by 3
rotate column x=15 by 1
rotate column x=13 by 1
rotate column x=12 by 1
rotate column x=11 by 2
rotate column x=10 by 1
rotate column x=8 by 1
rotate column x=7 by 2
rotate column x=5 by 1
rotate column x=3 by 3
rotate column x=2 by 1
rotate column x=1 by 1
rotate column x=0 by 1
rect 39x1
rotate column x=44 by 2
rotate column x=42 by 2
rotate column x=35 by 5
rotate column x=34 by 2
rotate column x=32 by 2
rotate column x=29 by 2
rotate column x=25 by 5
rotate column x=24 by 2
rotate column x=19 by 2
rotate column x=15 by 4
rotate column x=14 by 2
rotate column x=12 by 3
rotate column x=9 by 2
rotate column x=5 by 5
rotate column x=4 by 2
rotate row y=5 by 5
rotate row y=4 by 38
rotate row y=3 by 10
rotate row y=2 by 46
rotate row y=1 by 10
rotate column x=48 by 4
rotate column x=47 by 3
rotate column x=46 by 3
rotate column x=45 by 1
rotate column x=43 by 1
rotate column x=37 by 5
rotate column x=36 by 5
rotate column x=35 by 4
rotate column x=33 by 1
rotate column x=32 by 5
rotate column x=31 by 5
rotate column x=28 by 5
rotate column x=27 by 5
rotate column x=26 by 3
rotate column x=25 by 4
rotate column x=23 by 1
rotate column x=17 by 5
rotate column x=16 by 5
rotate column x=13 by 1
rotate column x=12 by 5
rotate column x=11 by 5
rotate column x=3 by 1
rotate column x=0 by 1"""
screenSize = (6, 50)

#theInput = """rect 3x2
#rotate column x=1 by 1
#rotate row y=0 by 4
#rotate column x=1 by 1"""
#screenSize = (3, 7)

rectRegex = re.compile('rect (\d+)x(\d+)')
columnRegex = re.compile('rotate column x=(\d+) by (\d+)')
rowRegex = re.compile('rotate row y=(\d+) by (\d+)')

def printScreen(pScreenLists):
    screenRows = list(''.join(('#' if aChar else ' ') for aChar in aRow) for aRow in pScreenLists)
    screenStr = '\n'.join(aRow for aRow in screenRows)
    print(screenStr)

def rect(pScreen, width, height):
    for row in range(height):
        for column in range(width):
            pScreen[row][column] = 1

def rotRow(pScreen, row, shift):
    for i in range(shift):
        pScreen[row] = [pScreen[row][len(pScreen[row])-1]] + pScreen[row][0:len(pScreen[row])-1]

def rotCol(pScreen, col, shift):
    for i in range(shift):
        bufPixel = pScreen[len(pScreen)-1][col]
        for j in range(len(pScreen)-1, 0, -1):
            pScreen[j][col] = pScreen[j-1][col]
        pScreen[0][col] = bufPixel

theScreen = list(list(0 for column in range(screenSize[1])) for column in range(screenSize[0]))
theInput = theInput.split('\n')
for line in theInput:
    # trict: the 8th character is on a fixed location and can help indicate the right command
    if line[7] == 'r':  # row rotation
        matches = rowRegex.match(line)
        theRow = int(matches.group(1))
        shiftNumber = int(matches.group(2))
        rotRow(theScreen, theRow, shiftNumber)
    elif line[7] == 'c':  # column rotation
        matches = columnRegex.match(line)
        theColumn = int(matches.group(1))
        shiftNumber = int(matches.group(2))
        rotCol(theScreen, theColumn, shiftNumber)
    else:  # rectangle
        matches = rectRegex.match(line)
        theWidth = int(matches.group(1))
        theHeight = int(matches.group(2))
        rect(theScreen, theWidth, theHeight)


printScreen(theScreen)
totSum = 0
for aRow in theScreen:
    totSum += sum(aPix for aPix in aRow)
print(totSum)
