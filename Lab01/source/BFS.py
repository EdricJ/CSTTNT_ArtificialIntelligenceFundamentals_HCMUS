import copy

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
        
def BFS(matrix, start, end):
    close = []
    open = [start]   
    bfsPath = {}

    while len(open) > 0:
        currPoint = open.pop(0)
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
        
                open.append(childPoint)
                bfsPath[childPoint] = currPoint

    if checkKey(bfsPath, end):
        path = {}
        point = end
        while point != start:
            path[bfsPath[point]] = point
            point = bfsPath[point]
        
        res = []
        res = list(path.values())
        res.append(end)
        res.reverse()

    else:
        res = None

    return res
