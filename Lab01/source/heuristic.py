import math

def heuristic(point_1, point_2, name):
    if name == 'Manhattan':
        x1, y1 = point_1
        x2, y2 = point_2
        h = abs(x1 - x2) + abs(y1 - y2)

    if name == 'Euclidean':
        x1, y1 = point_1
        x2, y2 = point_2
        h = math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))

    return h