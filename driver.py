# Lee's Algorithm is a fill algorithm that doesnt use recursion, but a buffer queue instead
import numpy as np
from collections import deque

mat = [
[[], [], [], [], [], []],       # 0
[[], [], [], [], [], [], []],   # 1
[[], [], [], [], [], []],       # 2
[[], [], [], [], [], [], []],   # 3
[[], [], [], [], [], []],       # 4
[[], [], [], [], [], [], []],   # 5
[[], [], [], [], [], []]        # 6
]
# even rows --> 0 - 5 (6)
# odd rows --> 0 - 6 (7) 
source = [0, 0]
# (x, y, color)

# color = 4 --> no pixel here
# color = 0 --> white
# color = 1 --> yellow
# color = 2 --> purple
# color = 3 --> green

# mat = pixel matrix
def fill(mat, source):
    q = deque()
    sum = 0
    def recursion(current):
        x = current[0]
        y = current[1]
        color = current[2]
        
        if mat[x][y + 1][2] == color:
            mat[x][y + 1][2] = 4
            sum += 1
            recursion([x, y + 1, color])
            
        if mat[x][y - 1][2] == color:
            mat[x][y - 1][2] = 4
            sum += 1
            recursion([x, y - 1, color])
            
        if mat[x + 1][y][2] == color:
            mat[x + 1][y][2] = 4
            sum += 1
            recursion([x + 1, y, color])
            
        if mat[x - 1][y][2] == color:
            mat[x - 1][y][2] = 4
            sum += 1
            recursion([x - 1, y, color])
            
        if mat[x + 1][y + 1][2] == color:
            mat[x + 1][y + 1][2] = 4
            sum += 1
            recursion([x + 1, y + 1, color])
            
        if mat[x + 1][y - 1][2] == color:
            mat[x + 1][y - 1][2] = 4
            sum += 1
            recursion([x + 1, y - 1, color])
            
    recursion(source)
        
def calculate_score():
    
        
    