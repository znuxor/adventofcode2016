#!/usr/bin/env python3

import re
from inputNine import getInput

theInput = getInput()
#theInput = '(3x3)XYZ'
#theInput = '(27x12)(20x12)(13x14)(7x10)(1x12)A'
#theInput = 'X(7x2)(3x3)ABCY'
#theInput = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'
numMatcher = re.compile('\((\d+)x(\d+)\)')

def expand(theString):
    """This function returns the number of characters in a fully expanded string"""

    # case 1: fully expanded. Check if there is parentheses, if not, then just return the length of the string
    if '(' not in theString:
        return len(theString)  # so smooooooooooth 8)

    # case 2: starts with a compression group that deals with all the string,
    #         in this case we need to force expansion to prevent infinite recursion
    
    ## 1: find the substring at the start, if any, that is already fully expanded
    theFirstIndex = 0
    while(theString[theFirstIndex] != '('):
        theFirstIndex+=1
    if theFirstIndex == 0:
        indexOpen = theFirstIndex
        indexClose = indexOpen+1
        while theString[indexClose] != ')':
            indexClose+=1
        indexClose+=1
        theMatch = numMatcher.match(theString[indexOpen:indexClose])
        numChar = int(theMatch.group(1))
        if indexClose+numChar == len(theString):
            ### NOW we know we're in case 2
            numTimes = int(theMatch.group(2))
            #print('case 2: I call expand with {}'.format(theString[indexClose:]))
            theMult = numTimes * expand(theString[indexClose:])
            #print('got {} from expand, I am {}'.format(theMult//numTimes, theString))
            #print('theMult for {} is {}'.format(theString, theMult))
            return theMult
    
    # case 3: not fully expanded and has some start stuff, then 3 things to do

    ## 1: find the substring at the start, if any, that is already fully expanded
    theFirstIndex = 0
    while(theString[theFirstIndex] != '('):
        theFirstIndex+=1
    lengthP1 = theFirstIndex

    ## 2: for every subgroup, expand them
    anIndex = theFirstIndex
    expandedSum = 0
    while(')' in theString[anIndex:]):
        indexOpen = anIndex
        while theString[indexOpen] != '(':
            indexOpen+=1
            expandedSum+=1
        # find the subgroup expansion string
        indexClose = indexOpen+1
        while theString[indexClose] != ')':
            indexClose+=1
        indexClose+=1
        #print(theString[indexOpen:indexClose])
        theMatch = numMatcher.match(theString[indexOpen:indexClose])
        numChar = int(theMatch.group(1))
        indexEndSubString=indexClose+numChar
        #print('case 3: I call expand with {}'.format(theString[indexOpen:indexEndSubString]))
        expandedSum += expand(theString[indexOpen:indexEndSubString])

        anIndex = indexEndSubString

    ## 3: find the length of the remaining fully expanded part, if any
    lengthP3 = len(theString)-anIndex
    theSum = lengthP1+expandedSum+lengthP3
    #print(lengthP1, expandedSum, lengthP3)
    #print('theSum for {} is {}'.format(theString, theSum))
    return theSum

print(expand(theInput))
