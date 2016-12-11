#!/usr/bin/env python3
import numpy
from copy import deepcopy

visitedStates = []
nodeNumber = 0


class State():
    def __init__(self, floor, genM, chM):
        self.floor = floor
        self.genM = genM
        self.chM = chM
        self.pairVector = numpy.sum(numpy.logical_and(genM, chM), 1)
        self.singleChipVector = numpy.sum(chM, 1) - self.pairVector
        self.singleGenVector = numpy.sum(genM, 1) - self.pairVector

    def __eq__(self, other):
        # return ((self.pairVector == other.pairVector).all() and
        #         (self.singleChipVector == other.singleChipVector).all() and
        #         (self.singleGenVector == other.singleGenVector).all())
        return ((self.pairVector == other.pairVector).all() and
                (self.singleChipVector == other.singleChipVector).all() and
                #(self.genM == other.genM).all() and
                #(self.chM == other.chM).all() and
                (self.floor == other.floor) and
                (self.singleGenVector == other.singleGenVector).all())


class Node():
    def __init__(self, depth, floor, genM, chM, parentNode):
        self.depth = depth
        self.floor = floor
        self.genM = deepcopy(genM)
        self.chM = deepcopy(chM)
        self.visited = False
        if parentNode is not None:

            self.parentNode = parentNode
        else:
            self.parentNode = self
        global nodeNumber
        self.nodeNumber = nodeNumber
        nodeNumber += 1
        self.childs = []
        # print('New node: # {}'.format(self.nodeNumber))
        # visitedMatrices.append(self.genM+self.chM)
        if numpy.sum(self.chM) + numpy.sum(self.genM) != 10:
            print(self.nodeNumber, self.floor)
            print('genM, chM')
            print(self.genM)
            print(self.chM)
            raise Exception("something is wrong!")
        if self.isWinner():
            raise Exception("found a winner at it. {}".format(self.depth))

    def isSafe(self):
        chipsWithProtection = numpy.multiply(self.genM, self.chM)
        chipsWithoutProtection = self.chM-chipsWithProtection
        vulnerableChipNumberPerFloor = numpy.sum(chipsWithoutProtection, 1)
        generatorNumberPerFloor = numpy.sum(self.genM, 1)
        if self.nodeNumber == 2:
            # print(' node {} info: '.format(self.nodeNumber))
            # print(self.genM)
            # print(self.chM)
            # input()
            pass
        if ((numpy.multiply(vulnerableChipNumberPerFloor,
                            generatorNumberPerFloor)).any()):
            return False
        else:
            if (self.floor == self.parentNode.parentNode.floor and
               (self.chM == self.parentNode.parentNode.chM).all() and
               (self.genM == self.parentNode.parentNode.genM).all()):
                # print('bop')
                return False
        aState = State(self.floor, self.genM, self.chM)
        if aState in visitedStates:
            return False
        else:
            visitedStates.append(aState)
            return True

    def isWinner(self):
        return (numpy.sum(self.chM, 1)[3] == 5 and
                numpy.sum(self.genM, 1)[3] == 5)

    def grow(self):
        if not self.visited:
            possibleFloors = [self.floor+1, self.floor-1]
            if possibleFloors[0] > 3:
                possibleFloors.pop(0)

            elif possibleFloors[1] < 0:
                possibleFloors.pop(1)

            # 1: try to move only a generator or two
            for pos1 in range(5):
                for pos2 in range(pos1, 5):
                    genPosVec = numpy.logical_or(numpy.array(range(5)) == pos1,
                                                 numpy.array(range(5)) == pos2)
                    genPosVec = genPosVec*1
                    if (numpy.sum(numpy.multiply(genPosVec,
                                                 self.genM[self.floor]))
                       == numpy.sum(genPosVec)).all():
                        subGenM = self.genM
                        # print(self.genM)
                        subGenM[self.floor] = self.genM[self.floor]-genPosVec
                        # print(subGenM)
                        for floor in possibleFloors:
                            subGenM[floor] = self.genM[floor]+genPosVec
                            newChild = Node(self.depth+1, floor, subGenM,
                                            self.chM, self)
                            if newChild.isSafe():
                                self.childs.append(newChild)
                            subGenM[floor] = self.genM[floor]-genPosVec
                        subGenM[self.floor] = self.genM[self.floor]+genPosVec

            # 2: try to move only a chip
            for pos1 in range(5):
                for pos2 in range(pos1, 5):
                    chPosVec = (numpy.array(range(5)) == pos1)*1
                    chPosVec = numpy.logical_or(numpy.array(range(5)) == pos1,
                                                numpy.array(range(5)) == pos2)
                    chPosVec = chPosVec*1
                    if (numpy.sum(numpy.multiply(chPosVec,
                                                 self.chM[self.floor]))
                            == numpy.sum(chPosVec)).all():
                        subChM = self.chM
                        # print(self.genM)
                        subChM[self.floor] = self.chM[self.floor]-chPosVec
                        # print(subGenM)
                        for floor in possibleFloors:
                            subChM[floor] = self.chM[floor]+chPosVec
                            newChild = Node(self.depth+1, floor, self.genM,
                                            subChM, self)
                            if newChild.isSafe():
                                self.childs.append(newChild)
                            subChM[floor] = self.chM[floor]-chPosVec
                        subChM[self.floor] = self.chM[self.floor]+chPosVec

            # 3: try to move a chip and a generator
            for pos1 in range(5):
                for pos2 in range(5):
                    genPosVec = (numpy.array(range(5)) == pos1)*1
                    chPosVec = (numpy.array(range(5)) == pos2)*1
                    if (numpy.multiply(genPosVec,
                        self.genM[self.floor]).any() and
                       numpy.multiply(chPosVec, self.chM[self.floor]).any()):
                        subGenM = self.genM
                        subChM = self.chM
                        subGenM[self.floor] = self.genM[self.floor]-genPosVec
                        subChM[self.floor] = self.chM[self.floor]-chPosVec
                        for floor in possibleFloors:
                            subGenM[floor] = self.genM[floor]+genPosVec
                            subChM[floor] = self.chM[floor]+chPosVec
                            newChild = Node(self.depth+1, floor, subGenM,
                                            subChM, self)
                            if newChild.isSafe():
                                self.childs.append(newChild)
                            subGenM[floor] = self.genM[floor]-genPosVec
                            subChM[floor] = self.chM[floor]-chPosVec
                        subGenM[self.floor] = self.genM[self.floor]+genPosVec
                        subChM[self.floor] = self.chM[self.floor]+chPosVec
            global treatedNode
            treatedNode += 1
            # print('finished treating node {}'.format(self.nodeNumber))
            # print('number of children: {}'.format(len(self.childs)))
            # print('parent node: {}'.format(self.parentNode.nodeNumber))
            # print(self.genM)
            # print(self.chM)
            self.visited = True
        else:
            # print("I am node {} with {} childs".format(self.nodeNumber,
            #                                            len(self.childs)))
            # print(self.genM)
            # print(self.chM)
            for child in self.childs:
                child.grow()


# promethium, cobalt, curium, ruthenium, plutonium
theInputGenerators = [[True, False, False, False, False],
                      [False, True, True, True, True],
                      [False, False, False, False, False],
                      [False, False, False, False, False]]
theInputChips = [[True, False, False, False, False],
                 [False, False, False, False, False],
                 [False, True, True, True, True],
                 [False, False, False, False, False]]

tIG = numpy.array(theInputGenerators, dtype=int)
tIC = numpy.array(theInputChips, dtype=int)
currentFloor = 1

rootNode = Node(0, 0, tIG, tIC, None)

treatedNode = 0

for i in range(40):
    print('iteration {}'.format(i))
    treatedNode = 0
    rootNode.grow()
    if treatedNode == 0:
        print('done at iteration {}'.format(i))
        break
