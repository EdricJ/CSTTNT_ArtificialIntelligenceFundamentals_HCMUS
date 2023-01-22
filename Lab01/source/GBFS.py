from ast import operator
import math
from queue import PriorityQueue
from tabnanny import check
from turtle import color
from unicodedata import name
from heuristic import heuristic

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

def GBFS(matrix, start, end, h):
    pointList = []
    open = []
    greedyPath = {}

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            pointList.append((i, j))

    f = {point : float('inf') for point in pointList}
    f[start] = heuristic(start, end, h)

    explored = PriorityQueue()
    explored.put((heuristic(start, end, h), start))

    while not explored.empty(): 
        currPoint = explored.get()[1]
        open.append(currPoint)

        if currPoint == end:
            break

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
                if childPoint in open:
                    continue

                f[childPoint] = heuristic(childPoint, end, h)
                explored.put((heuristic(childPoint, end, h), childPoint))            
                greedyPath[childPoint] = currPoint
        

    if checkKey(greedyPath, end):
        path = {}
        point = end
        while point != start:
            path[greedyPath[point]] = point
            point = greedyPath[point]

        res = []
        res = list(path.values())
        res.append(end)
        res.reverse()

    else:
        res = None

    return res