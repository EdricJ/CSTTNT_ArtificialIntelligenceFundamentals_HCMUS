import os
import os.path as p
from pathlib import Path
from read_file import read_file, read_file_2
from teleport import maze_have_teleportations
from visualize_maze import visualize_maze
from draw_maze import draw_maze
from DFS import DFS
from BFS import BFS
from UCS import UCS
from AStar import aStar
from GBFS import GBFS
from bonus import maze_have_points
from create_video import create_video

def solve_maze(algo, level, map, heuristic = None):
    openTele = []
    lv = 'level_' + str(level)
    cur = p.dirname(Path(__file__).parent.absolute())  #lấy directory
    

    if level == 3:
        lv = 'advance'
        levelDirectory = cur + '\\input\\' + lv + '\\'
        name = p.join(levelDirectory,map)
        bonus_points = []
        teleportations, matrix = read_file_2(name)
    else:
        levelDirectory = cur + '\\input\\' + lv + '\\'
        name = p.join(levelDirectory,map)
        teleportations = {}
        bonus_points, matrix = read_file(name)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=='S':
                start=(i,j)

            elif matrix[i][j]==' ':
                if (i==0) or (i==len(matrix)-1) or (j==0) or (j==len(matrix[0])-1):
                    end=(i,j)
                
            else:
                pass
    if level == 1:            
        if (algo == 'DFS'):   
            route = DFS(matrix, start, end)
            cost = len(route)
        elif (algo == 'BFS'):
            route = BFS(matrix, start, end)
            cost = len(route)
        elif (algo == 'UCS'):
            route = UCS(matrix, start, end)
            cost = len(route)
        elif (algo == 'AStar'):
            route = aStar(matrix, start, end, heuristic)
            cost = len(route)
        elif (algo == 'GBFS'):
            route = GBFS(matrix, start, end, heuristic)
            cost = len(route)
    if level == 2:
        route, s = maze_have_points(matrix, start, end, bonus_points)
        cost = len(route) + s

    if level == 3:
        route, openTele = maze_have_teleportations(matrix, start, end, teleportations, 'Manhattan')
        cost = len(route)

    walls = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == 'x']
    visualize_maze(matrix, bonus_points, start, end, openTele, route, cost, algo, lv, map, heuristic)
    create_video(start, end, route, bonus_points, teleportations, walls, algo, lv, map, heuristic)