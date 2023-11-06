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
source = [0, 0, 0]
# (x, y, color)

# color = 4 --> no pixel here
# color = 0 --> white
# color = 1 --> yellow
# color = 2 --> purple
# color = 3 --> green

# mat = pixel matrix
# N = size of matrix
def lee_fill(mat, cols, source):
    def findNeighbors(mat, current):
        x = current[0]
        y = current[1]
        color = current[2]
        if mat[x][y + 1][2] == 
    q = deque()
    q.append(source)
    while q:
        current = q.popleft()
        
    