from queue import PriorityQueue
from heuristic import heuristic

def isInList(point, route):
    for item in route:
        if item == point:
            return True
    return False

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

def maze_have_teleportations(matrix, start, end, teleportations, h):
    pointList = []
    telePath = {}
    close = []
    inTeleport = []
    openTele = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            pointList.append((i, j))

    inTeleport = list(teleportations.keys())

    g = {point : float('inf') for point in pointList}
    g[start] = 0
    f = {point : float('inf') for point in pointList}
    f[start] = heuristic(start, end, h)

    open = PriorityQueue()
    open.put((heuristic(start, end, h), heuristic(start, end, h), start))

    while not open.empty():
        currPoint = open.get()[2]
        if currPoint == end:
            break
        if currPoint in close:
            continue
        close.append(currPoint)

        isTeleported = False
        a, b = currPoint
        for dir in 'ESNW':
            if checkDirection(matrix, currPoint, dir):
                if dir == 'E':
                    childPoint = (a, b+1)
                if dir == 'W':
                    childPoint = (a, b-1)
                if dir == 'S':
                    childPoint = (a+1, b)
                if dir == 'N':
                    childPoint = (a-1, b)
                
                if isInList(currPoint, inTeleport):
                    if heuristic(teleportations[currPoint], end, h) < heuristic(childPoint, end, h):
                        childPoint = teleportations[currPoint]
                        gTmp = g[currPoint]
                        isTeleported = True
                    else:
                        gTmp = g[currPoint] + 1
                else:
                    gTmp = g[currPoint] + 1

                fTmp = gTmp + heuristic(childPoint, end, h)

                if fTmp < f[childPoint]:
                    g[childPoint] = gTmp
                    f[childPoint] = fTmp
                    open.put((fTmp, heuristic(childPoint, end, h), childPoint))
                    telePath[childPoint] = currPoint
                    if isTeleported:
                        openTele.append(currPoint)
                        isTeleported = False
    
    if checkKey(telePath, end):
        path = {}
        point = end
        while point != start:
            path[telePath[point]] = point
            point = telePath[point]

        res = []
        res = list(path.values())
        res.append(end)
        res.reverse()

    else:
        res = None 

    return res, openTele