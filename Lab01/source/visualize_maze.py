import os.path as p
from pathlib import Path
import matplotlib.pyplot as plt
from ast import operator
import math
from queue import PriorityQueue
from tabnanny import check
from turtle import color
from unicodedata import name

def isInList(point, route):
    for item in route:
        if item == point:
            return True
    return False

def visualize_maze(matrix, bonus, start, end, openTele=None, route = None, cost = None, algo = None, level = None, map = None, heuristic = None):
    """
    Args:
      1. matrix: The matrix read from the input file,
      2. bonus: The array of bonus points,
      3. start, end: The starting and ending points,
      4. open: The open from the starting point to the ending one, defined by an array of (x, y), e.g. open = [(1, 2), (1, 3), (1, 4)]
    """
    #1. Define walls and array of direction based on the open
    walls=[(i,j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j]=='x']
    inTeleport = []
    outTeleport = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'i':
                inTeleport.append((i, j))
            if matrix[i][j] == 'o':
                outTeleport.append((i, j))

    if route:
        direction=[]
        for i in range(1, len(route)):      
            if isInList(route[i-1], openTele):
                direction.append('None')
            else:
                if route[i][0]-route[i-1][0] > 0:
                    direction.append('v') #^
                elif route[i][0]-route[i-1][0] < 0:
                    direction.append('^') #v        
                elif route[i][1]-route[i-1][1] > 0:
                    direction.append('>')
                else:
                    direction.append('<')
        direction.pop(0)  

    #2. Drawing the map
    ax = plt.figure(dpi=100).add_subplot(111)

    for i in ['top','bottom','right','left']:
        ax.spines[i].set_visible(False)


    plt.scatter([i[1] for i in walls],[-i[0] for i in walls],
                marker='X',s=100,color='black')
                
    plt.scatter([i[1] for i in inTeleport],[-i[0] for i in inTeleport],
                marker='d',s=100,color='pink')
    plt.scatter([i[1] for i in outTeleport],[-i[0] for i in outTeleport],
                marker='d',s=100,color='purple')

    plt.scatter([i[1] for i in bonus],[-i[0] for i in bonus],
                marker='P',s=100,color='green')

    plt.scatter(start[1],-start[0],marker='*',
                s=100,color='orange')

    if route:
        for i in range(len(route)-2):
            plt.scatter(route[i+1][1],-route[i+1][0],
                        marker=direction[i],color='orchid')


    plt.text(end[1],-end[0],'EXIT',color='red',
         horizontalalignment='center',
         verticalalignment='center')

    text = 'Cost: ' + str(cost)
    plt.text(1, 1, text, color='black', horizontalalignment='center')

    if route == None:
        error = 'UNABLE TO FIND PATH'
        plt.text(35, 1, error, color='red', horizontalalignment='center', fontsize = 12)
    

    plt.xticks([])
    plt.yticks([])
   

    print(f'Starting point (x, y) = {start[0], start[1]}')
    print(f'Ending point (x, y) = {end[0], end[1]}')
    
    for _, point in enumerate(bonus):
      print(f'Bonus point at position (x, y) = {point[0], point[1]} with point {point[2]}')

    #3. Output
    map = map.strip(".txt")
    
    cur = p.dirname(Path(__file__).parent.absolute())  #lấy directory
    
    #Tạo folder mới

    new_folder = cur + '\\output\\' + level + '\\' + map + '\\'
    Path(new_folder).mkdir(parents = True, exist_ok = True)

    if (heuristic):
        if heuristic == 'Manhattan':
                folder = new_folder + algo + '\\'
                name_png = algo +'_heuristic_1.jpg'
        elif heuristic == 'Euclidean':
                folder = new_folder + algo + '\\'
                name_png = algo +'_heuristic_2.jpg'
    else:
        folder = new_folder + algo + '\\'
        name_png = algo + '.jpg'
        


    figure = plt.gcf()
    figure.set_size_inches(18, 10)
    Path(folder).mkdir(parents = True, exist_ok = True)
    plt.savefig(p.join(folder, name_png), bbox_inches='tight')

    name_txt = algo + '.txt'
    with open(p.join(folder,name_txt), 'w') as outfile:
        outfile.write(str(cost))


    plt.show()