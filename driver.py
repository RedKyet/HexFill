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
    # mode = 0 --> empty (score calculation, kill bombs)
    # mode = 1 --> blanks (bleaching bombs)
    # mode = 2, 3 or 4 --> superfill (color bombs)
    
    sum = 0
    def recursion(current):
        nonlocal sum
        nonlocal mat
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
    return [sum, mat]
        
def master(mat, prev_score):
    def calculate_score(mat):
        score = 0
        highest_area = 0
        highest_color = 0

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j][2] != 0 and mat[i][j][2] != 1:
                    color = mat[i][j][2]
                    add = fill(mat, [i, j, mat[i][j][2]], 0)[0]
                    
                    if add >= highest_area:
                        highest_area = add
                        highest_color = color
                        
                    score += add ** 2
        return [score, highest_area, highest_color]
    
    result = calculate_score(mat)
    score = result[0]
    highest_area = result[1]
    highest_color = result[2]
    
    score_diff = score - prev_score
    
    score_TEXT = str(score)
    score_diff_TEXT = '+ ' + str(score_diff)
    if(score_diff > 5):
        score_diff_TEXT += ' Combo!'
        
    highest_TEXT = ''
    if highest_color == 2:
        highest_TEXT = 'Cea mai mare zonă este galbenă! (' + str(highest_area) + ' pixeli)'
    elif highest_color == 3:
        highest_TEXT = 'Cea mai mare zonă este mov! (' + str(highest_area) + ' pixeli)'
    elif highest_color == 4:
        highest_TEXT = 'Cea mai mare zonă este verde! (' + str(highest_area) + ' pixeli)'
    # elif highest_color == 5:
    #     highest_TEXT = '-1'
    
    return [score_TEXT, score_diff_TEXT, highest_TEXT]

def bomb(mat, source):
    mat = fill(mat, source, 0)[1]
    return mat
    
def bleach(mat, source):
    mat = fill(mat, source, 1)[1]
    return mat

def color(mat, source, mode):
    mat = fill(mat, source, mode)[1]
    return mat

test_mat = [
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],  # 0 (TOP)
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],             # 1
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],  # 2
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],             # 3
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],  # 4
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 4], [0, 0, 4], [0, 0, 4]],             # 5
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 4], [0, 0, 4], [0, 0, 4], [0, 0, 1]],  # 6
[[0, 0, 0], [0, 0, 0], [0, 0, 4], [0, 0, 4], [0, 0, 1], [0, 0, 1]],             # 7
[[0, 0, 0], [0, 0, 4], [0, 0, 3], [0, 0, 1], [0, 0, 1], [0, 0, 3], [0, 0, 2]],  # 8
[[0, 0, 4], [0, 0, 4], [0, 0, 3], [0, 0, 1], [0, 0, 3], [0, 0, 2]],             # 9
[[0, 0, 1], [0, 0, 3], [0, 0, 3], [0, 0, 3], [0, 0, 2], [0, 0, 3], [0, 0, 3]],  # 10
[[0, 0, 1], [0, 0, 1], [0, 0, 3], [0, 0, 3], [0, 0, 3], [0, 0, 3]],             # 11 (BOTTOM)
]
text = master(test_mat, 0)
print(text[0])
print(text[1])
print(text[2])