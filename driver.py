# Lee's Algorithm is a fill algorithm that doesnt use recursion, but a buffer queue instead
import numpy as np
from collections import deque

# test_mat = [
# [[], [], [], [], [], []],       # 0
# [[], [], [], [], [], [], []],   # 1
# [[], [], [], [], [], []],       # 2
# [[], [], [], [], [], [], []],   # 3
# [[], [], [], [], [], []],       # 4
# [[], [], [], [], [], [], []],   # 5
# [[], [], [], [], [], []]        # 6
# [[], [], [], [], [], [], []],   # 7
# [[], [], [], [], [], []]        # 8
# [[], [], [], [], [], [], []],   # 9
# [[], [], [], [], [], []]        # 10
# [[], [], [], [], [], [], []],   # 11
# ]

test_mat = [
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],                 # 0
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],      # 1
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],                 # 2
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],      # 3
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],                 # 4
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],      # 5
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],                 # 6
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],      # 7
[[0, 0, 0], [0, 0, 0], [3, 3, 3], [0, 0, 0], [0, 0, 0], [0, 0, 0]],                 # 8
[[0, 0, 0], [0, 0, 0], [3, 3, 3], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],      # 9
[[1, 1, 1], [3, 3, 3], [3, 3, 3], [3, 3, 3], [0, 0, 0], [0, 0, 0]],                 # 10
[[1, 1, 1], [1, 1, 1], [3, 3, 3], [3, 3, 3], [0, 0, 0], [0, 0, 0], [0, 0, 0]],      # 11
]

# even rows --> 0 - 5 (6)
# odd rows --> 0 - 6 (7) 
source = [0, 0]
# (x, y, color)

# color = 0 --> no pixel here
# color = 1 --> white
# color = 2 --> yellow
# color = 3 --> purple
# color = 4 --> green

# mat = pixel matrix
def fill(mat, source, mode):
    # mode = 0 --> empty (score calculation)
    # mode = 1 --> blanks (bleaching bombs)
    # mode = 2, 3 or 4 --> superfill (color bombs)
    
    q = deque()
    sum = 0
    def recursion(current):
        nonlocal sum
        x = current[0]
        y = current[1]
        color = current[2]
        
        if(y + 1 < len(mat[x])): 
            if mat[x][y + 1][2] == color:
                mat[x][y + 1][2] = mode
                sum += 1
                recursion([x, y + 1, color])
            
        if(y - 1 >= 0):    
            if mat[x][y - 1][2] == color:
                mat[x][y - 1][2] = mode
                sum += 1
                recursion([x, y - 1, color])
           
        if(x + 1 < len(mat)):    
            if mat[x + 1][y][2] == color:
                mat[x + 1][y][2] = mode
                sum += 1
                recursion([x + 1, y, color])
        
        if(x - 1 >= 0):   
            if mat[x - 1][y][2] == color:
                mat[x - 1][y][2] = mode
                sum += 1
                recursion([x - 1, y, color])
        
        if(x + 1 < len(mat) and y + 1 < len(mat[x])):    
            if mat[x + 1][y + 1][2] == color:
                mat[x + 1][y + 1][2] = mode
                sum += 1
                recursion([x + 1, y + 1, color])
            
        if(x + 1 < len(mat) and y - 1 >= 0):
            if mat[x + 1][y - 1][2] == color:
                mat[x + 1][y - 1][2] = mode
                sum += 1
                recursion([x + 1, y - 1, color])
            
    recursion(source)
    return sum
        
def calculate_score(mat):
    score = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j][2] != 0 and mat[i][j][2] != 1:
                score += max(1, fill(mat, [i, j, mat[i][j][2]], 0)) ** 2
    return score

def bleach(mat, source):
    fill(mat, source, 1)

def color(mat, source, mode):
    fill(mat, source, mode)

# print(calculate_score(test_mat))