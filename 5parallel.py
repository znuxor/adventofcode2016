#!/usr/bin/env python3
from hashlib import md5
import sys
from multiprocessing import Pool
import math
theInput = "uqwqemis"
def findchars(start, step):
    theKey = []
    theInteger = start 
    while len(theKey) < 8:
        theString = theInput + str(theInteger)
        m = md5()
        m.update(bytes(theString, 'ascii'))
        theHash = list(m.digest())
        if theHash[0] == 0 and theHash[1] == 0 and theHash[2]//16 ==0:
            theKey.append((theHash[2]%16))
            print("char found at " + str(theInteger))
            print("the char is {:01x} ".format((theHash[2]%16)))
        theInteger += step
    return theKeys
nProc = 8
aPool = Pool(processes=nProc)
for i in range(nProc):
    aPool.apply_async(findchars, (i, nProc))

aPool.close()
aPool.join()
