from copy import deepcopy
from operator import truediv
from heuristic import heuristic
from ast import operator
import math
from queue import PriorityQueue
from tabnanny import check
from turtle import color
from unicodedata import name

def isInRoute(point, route, start):
    copy = deepcopy(route)
    copy.insert(0,start)
    for item in copy:
        if item == point:
            return True
    return False

def checkDirection(matrix, point, dir, route, start):
    a, b = point
    if matrix[a][b+1] != 'x' and (not isInRoute((a,b+1), route, start)) and dir == 'E':
        return True
    elif matrix[a+1][b] != 'x' and (not isInRoute((a+1,b), route, start)) and dir == 'S':
        return True
    elif matrix[a-1][b] != 'x' and (not isInRoute((a-1,b), route, start)) and dir == 'N':
        return True
    elif matrix[a][b-1] != 'x' and (not isInRoute((a,b-1), route, start)) and dir == 'W':
        return True
    else:
        return False

def checkKey(dic, key):
    if key in dic.keys():
        return True
    else:
        return False
    
def aStar(matrix, start, end, h, route, s_point):
    pointList = []
    aStarPath = {}

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            pointList.append((i, j))

    g = {point : float('inf') for point in pointList}
    g[start] = 0
    f = {point : float('inf') for point in pointList}
    f[start] = heuristic(start, end, h)

    explored = PriorityQueue()
    explored.put((heuristic(start, end, h), heuristic(start, end, h), start))

    while not explored.empty():
        currPoint = explored.get()[2]
        if currPoint == end:
            break

        a, b = currPoint
        for dir in 'ESNW':
            if checkDirection(matrix, currPoint, dir, route, s_point):
                if dir == 'E':
                    childPoint = (a, b+1)
                if dir == 'W':
                    childPoint = (a, b-1)
                if dir == 'S':
                    childPoint = (a+1, b)
                if dir == 'N':
                    childPoint = (a-1, b)
                
                gTmp = g[currPoint] + 1
                fTmp = gTmp + heuristic(childPoint, end, h)

                if fTmp < f[childPoint]:
                    g[childPoint] = gTmp
                    f[childPoint] = fTmp
                    explored.put((fTmp, heuristic(childPoint, end, h), childPoint))
                    aStarPath[childPoint] = currPoint

    
    if checkKey(aStarPath, end):
        path = {}
        point = end
        while point != start:
            path[aStarPath[point]] = point
            point = aStarPath[point]
        
        res = []
        for item in path.values():
            res.append(item)
        res.append(end)
        res.reverse()
    else:
        res = None

    return res

def findPos(list, element):
    res = 0
    for i in range(0, len(list)):
        if list[i][0] == element[0] and list[i][1] == element[1]:
            res = i
    return res

def maze_have_points(matrix, start, end, bonus_point):
    route = []
    visited = [start]
    bonus = deepcopy(bonus_point)
    tmpBonus = {}
    score = 0
    h = 'Manhattan'
    removedBonus = []
     
    while True:
        s = start
        while len(bonus) > 0:
            for item in bonus:
                point = (item[0], item[1])
                tmpBonus.update({item : heuristic(s, point, h)})

            tmp = min(tmpBonus, key = tmpBonus.get)
            tmpEnd = (tmp[0], tmp[1])
            tmpScore = tmp[2]
            tmpBonus.pop(tmp)   
            bonus.remove(tmp)   

            tmpRoute = aStar(matrix, s, tmpEnd, h, route, start)
            if tmpRoute != None:
                tmpRoute.pop(0)
                route = route + tmpRoute
                score = score + tmpScore
                s = tmpEnd
                visited.append(s)

        tmpRoute = aStar(matrix, s, end, h, route, start)
        if tmpRoute != None:
            tmpRoute.pop(0)
            route = route + tmpRoute
            route.insert(0, start)
            break
        else:
            point = visited[len(visited) - 1]
            removedBonus.append(point)
            bonus = deepcopy(bonus_point)

            for item in removedBonus:
                bonus.pop(findPos(bonus, item))

            visited = []
            route = []
            score = 0
 
    return route, score
        