from solve_maze import *
import os
from create_folder import createFolder

#Create input output folder and draw maps
createFolder()

#Get all files in input level_1
curPath = p.dirname(Path(__file__).parent.absolute())
inputLevel1 = os.listdir(Path(curPath + '\\input\\' + '\\level_1\\'))
   
#Get all files in input level_2
curPath = p.dirname(Path(__file__).parent.absolute())
inputLevel2 = os.listdir(Path(curPath + '\\input\\' + '\\level_2\\'))

#Get all files in input advance
curPath = p.dirname(Path(__file__).parent.absolute())
inputAdvance = os.listdir(Path(curPath + '\\input\\' + '\\advance\\'))

#Algorithm level map heuristic
'''
for i in ['DFS', 'BFS', 'UCS']:
    for j in inputLevel1:
        solve_maze(i, 1, j)

for i in ['AStar', 'GBFS']:
    for j in inputLevel1:
        for k in ['Euclidean', 'Manhattan']:
            solve_maze(i, 1, j, k)
'''
for i in inputLevel2:
    solve_maze('Bonus', 2, i)   
'''
for i in inputAdvance:
    solve_maze('Teleport', 3, i)
'''