#!/usr/bin/env python3

theInput = 1352
coordDest = (31, 39)
myMap = []
visitedLocs = []
pathLocs = []

def isWall(x, y, pInput):
    if x >= 0 and y >= 0:
        return sum(list(int(i) for
                        i in "{0:b}".format(x**2 + 3 * x + 2 * x * y
                                            + y + y * y + pInput))) % 2
    else:
        return 1


class Node():
    def __init__(self, pDepth, pPosX, pPosY, pParent):
        self.posX = pPosX
        self.posY = pPosY
        self.depth = pDepth
        self.childs = []
        visitedLocs.append((pPosX, pPosY))
        self.visited = False
        self.isWinner()
        # print('new at {} {}'.format(self.posX, self.posY))

    def isWinner(self):
        if (self.posX, self.posY) == coordDest:
            pathLocs.append((self.posX, self.posY))

            raise Exception("found a winner at depth {}".format(self.depth))

    def grow(self):
        if not self.visited:
            possiblePos = [(self.posX-1, self.posY),
                           (self.posX+1, self.posY),
                           (self.posX, self.posY-1),
                           (self.posX, self.posY+1)]
            for aPos in possiblePos:
                if (not isWall(*aPos, theInput) and
                   aPos not in visitedLocs):
                    try:
                        newChild = Node(self.depth+1, *aPos, self)
                    except Exception as e:
                        pathLocs.append((self.posX, self.posY))
                        raise Exception(e)
                    self.childs.append(newChild)
            self.visited = True
        else:
            for child in self.childs:
                try:
                    child.grow()
                except Exception as e:
                    pathLocs.append((self.posX, self.posY))
                    raise Exception(e)


# basically implement another BFS in a tree
rootNode = Node(0, 1, 1, None)
try:
    while(True):
        rootNode.grow()
except Exception as e:
    for y in range(45):
        myMap.append([])
        for x in range(45):
            myMap[y].append(isWall(x, y, theInput))
            if (x, y) in pathLocs:
                print("\033[92m"+str(myMap[y][x])+"\033[0m", end='')
            elif myMap[y][x]:
                print("\033[91m"+str(myMap[y][x])+"\033[0m", end='')
            else:
                print(myMap[y][x], end='')
        print()

    print(e)
    input()

visitedLocs = []
rootNode = Node(0, 1, 1, None)

for i in range(50):
    rootNode.grow()

for y in range(45):
    myMap.append([])
    for x in range(45):
        myMap[y].append(isWall(x, y, theInput))
        if (x, y) in visitedLocs:
            print("\033[92m"+str(myMap[y][x])+"\033[0m", end='')
        elif myMap[y][x]:
            print("\033[91m"+str(myMap[y][x])+"\033[0m", end='')
        else:
            print(myMap[y][x], end='')
    print()

print("location number is {}".format(len(visitedLocs)))

