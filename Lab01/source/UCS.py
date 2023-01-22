from queue import PriorityQueue

def checkDirection(matrix, point, dir):
    a, b = point
    if matrix[a][b+1] != 'x' and dir == 'E':
        return True
    elif matrix[a+1][b] != 'x' and dir == 'S':
        return True
    elif matrix[a-1][b] != 'x' and dir == 'N':
        return True
    elif matrix[a][b-1] != 'x' and dir == 'W':
        return True
    else:
        return False

def checkKey(dic, key):
    if key in dic.keys():
        return True
    else:
        return False
        
def UCS(matrix, start, end):
    pointList = []
    close = []
    ucsPath = {}
    open = PriorityQueue()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            pointList.append((i, j))

    open.put((0, start))

    while not open.empty():
        tmp = open.get()
        g = tmp[0]
        currPoint = tmp[1]

        if currPoint == end:
            break
        if currPoint in close:
            continue
        close.append(currPoint)

        a, b = currPoint
        for dir in 'ESNW':
            if checkDirection(matrix, currPoint, dir):
                if dir == 'E':
                    childPoint = (a, b+1)
                elif dir == 'W':
                    childPoint = (a, b-1)
                elif dir == 'S':
                    childPoint = (a+1, b)
                elif dir == 'N':
                    childPoint = (a-1, b)
                if childPoint in close:
                    continue

                tmpDist = g + 1
                open.put((tmpDist, childPoint))
                ucsPath[childPoint] = currPoint

    if checkKey(ucsPath, end):
        path = {}
        point = end
        while point != start:
            path[ucsPath[point]] = point
            point = ucsPath[point]

        res = []
        res = list(path.values())
        res.append(end)
        res.reverse()

    else:
        res = None

    return res