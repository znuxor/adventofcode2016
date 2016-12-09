#!/usr/bin/env python3

import re
from inputNine import getInput

theInput = getInput()
builtInput = ""
numMatcher = re.compile('(\d+)x(\d+)')

charPtr = 0
while charPtr < len(theInput):
    if theInput[charPtr] != "(":
        builtInput += theInput[charPtr]
        charPtr+=1
    else:
        charPtr2 = 0
        while theInput[charPtr+charPtr2] != ')':
            charPtr2+=1
        theCopyStr = theInput[charPtr+1:charPtr2+charPtr]
        charPtr = charPtr2+charPtr+1
        matches = numMatcher.match(theCopyStr)
        #print(theCopyStr)
        numChar = int(matches.group(1))
        numRep = int(matches.group(2))
        #print(numChar, numRep)
        strToRepeat = theInput[charPtr:charPtr+numChar]
        #print(strToRepeat, end=", ")
        for i in range(numRep):
            builtInput+= strToRepeat
        charPtr += numChar

print(builtInput)
print(len(builtInput))
