import os.path as p
from pathlib import Path

from draw_maze import draw_maze

def createFolder():
    cur = p.dirname(Path(__file__).parent.absolute())
    
    for i in ['level_1', 'level_2', 'advance']:
        #create folder input
        newFolder = cur + '\\input\\' + i + '\\'
        Path(newFolder).mkdir(parents = True, exist_ok = True)
        draw_maze(i)
        #create folder output
        newFolder = cur + '\\output\\' + i + '\\'
        Path(newFolder).mkdir(parents = True, exist_ok = True)