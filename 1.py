#!/usr/bin/env python3
theInput = "L1, L3, L5, L3, R1, L4, L5, R1, R3, L5, R1, L3, L2, L3, R2, R2, L3, L3, R1, L2, R1, L3, L2, R4, R2, L5, R4, L5, R4, L2, R3, L2, R4, R1, L5, L4, R1, L2, R3, R1, R2, L4, R1, L2, R3, L2, L3, R5, L192, R4, L5, R4, L1, R4, L4, R2, L5, R45, L2, L5, R4, R5, L3, R5, R77, R2, R5, L5, R1, R4, L4, L4, R2, L4, L1, R191, R1, L1, L2, L2, L4, L3, R1, L3, R1, R5, R3, L1, L4, L2, L3, L1, L1, R5, L4, R1, L3, R1, L2, R1, R4, R5, L4, L2, R4, R5, L1, L2, R3, L4, R2, R2, R3, L2, L3, L5, R3, R1, L4, L3, R4, R2, R2, R2, R1, L4, R4, R1, R2, R1, L2, L2, R4, L1, L2, R3, L3, L5, L4, R4, L3, L1, L5, L3, L5, R5, L5, L4, L2, R1, L2, L4, L2, L4, L1, R4, R4, R5, R1, L4, R2, L4, L2, L4, R2, L4, L1, L2, R1, R4, R3, R2, R2, R5, L1, L2".split(", ")

turns, lengths = zip(*list((i[0], i[1:]) for i in theInput))
lengths = list(int(i) for i in lengths)
x, y = 0, 0
dir = 'n'

visitList = [(0, 0)]
firstCoord = None

if len(lengths) != len(turns):
    raise Exception("non equal lists")

for i in range(len(turns)):
    if dir == 'n':
        if turns[i] == 'L':
            dir = 'w'
        elif turns[i] == 'R':
            dir = 'e'
    elif dir == 'w':
        if turns[i] == 'L':
            dir = 's'
        elif turns[i] == 'R':
            dir = 'n'
    elif dir == 's':
        if turns[i] == 'L':
            dir = 'e'
        elif turns[i] == 'R':
            dir = 'w'
    elif dir == 'e':
        if turns[i] == 'L':
            dir = 'n'
        elif turns[i] == 'R':
            dir = 's'

    if dir == 'n':
        for i in range(lengths[i]):
            y += 1
            if (x, y) in visitList and firstCoord is None:
                print(x, y)
                firstCoord = (x, y)
            visitList.append((x, y))
    elif dir == 's':
        for i in range(lengths[i]):
            y -= 1
            if (x, y) in visitList and firstCoord is None:
                print(x, y)
                firstCoord = (x, y)
            visitList.append((x, y))
    elif dir == 'w':
        for i in range(lengths[i]):
            x -= 1
            if (x, y) in visitList and firstCoord is None:
                print(x, y)
                firstCoord = (x, y)
            visitList.append((x, y))
    elif dir == 'e':
        for i in range(lengths[i]):
            x += 1
            if (x, y) in visitList and firstCoord is None:
                print(x, y)
                firstCoord = (x, y)
            visitList.append((x, y))

print("distance for first part:" + str(abs(x)+abs(y)))

print("distance for second part: " + str(abs(firstCoord[0])+abs(firstCoord[1])))

