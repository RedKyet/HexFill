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
    mat[source[0]][source[1]][2] = mode
    sum += 1
    def recursion(current):
        nonlocal sum
        x = current[0]
        y = current[1]
        color = current[2]
        
        dist6x = [-1,  1,  0,  0, -1,  1]
        dist6y = [ 0,  0, -1,  1,  1,  1]
        
        dist7x = [-1,  1,  0,  0, -1,  1]
        dist7y = [ 0,  0, -1,  1, -1, -1]
        
        if(x % 2 == 1):
            for i in range(6):
                if(x + dist6x[i] >= 0 and x + dist6x[i] < len(mat) and y + dist6y[i] >= 0 and y + dist6y[i] < len(mat[x + dist6x[i]])):
                    if mat[x + dist6x[i]][y + dist6y[i]][2] == color:
                        mat[x + dist6x[i]][y + dist6y[i]][2] = mode
                        sum += 1
                        recursion([x + dist6x[i], y + dist6y[i], color])
        else:
            for i in range(6):
                if(x + dist7x[i] >= 0 and x + dist7x[i] < len(mat) and y + dist7y[i] >= 0 and y + dist7y[i] < len(mat[x + dist7x[i]])):
                    if mat[x + dist7x[i]][y + dist7y[i]][2] == color:
                        mat[x + dist7x[i]][y + dist7y[i]][2] = mode
                        sum += 1
                        recursion([x + dist7x[i], y + dist7y[i], color])
            
    recursion(source)
    return [sum, mat]
        
def get_stats(mat, prev_score):
    def calculate_score(mat):
        score = 0
        highest_area = 0
        highest_color = 0

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j][2] != 0 and mat[i][j][2] != 1:
                    
                    color = mat[i][j][2]
                    add = fill(mat, [i, j, mat[i][j][2]], 0)[0]
                    
                    if add > highest_area:
                        highest_area = add
                        highest_color = color
                        
                    score += add ** 2
        return [score, highest_area, highest_color]
    
    result = calculate_score(mat)
    score = result[0]
    highest_area = result[1]
    highest_color = result[2]
    
    score_diff = score - prev_score
    
    if(score_diff > 0):
        score_diff_TEXT = '+ ' + str(score_diff) + ' pentru ultimul pixel plasat!'
    elif(score_diff == 0):
        score_diff_TEXT = 'Plaseaza un pixel!'
    else:
        score_diff_TEXT = '- ' + str(-score_diff) + ' pentru ultimul pixel plasat!'
    
    score_TEXT = str(score)
    
    if(score_diff > 5):
        score_diff_TEXT += ' Combo!'
        
    highest_TEXT = ''
    if highest_color == 2:
        highest_TEXT = 'Cea mai mare zona este galbena! (' + str(highest_area) + ' pixeli)'
    elif highest_color == 3:
        highest_TEXT = 'Cea mai mare zona este mov! (' + str(highest_area) + ' pixeli)'
    elif highest_color == 4:
        highest_TEXT = 'Cea mai mare zona este verde! (' + str(highest_area) + ' pixeli)'
    # elif highest_color == 5:
    #     highest_TEXT = '-1'
    
    return [[score_TEXT, score_diff_TEXT, highest_TEXT], score, highest_color]

# def bomb(mat, source):
#     mat = fill(mat, source, 0)[1]
#     return mat
    
# def bleach(mat, source):
#     mat = fill(mat, source, 1)[1]
#     return mat

# def color(mat, source, mode):
#     mat = fill(mat, source, mode)[1]
#     return mat

test_mat = [
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],  # 0 (TOP)
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],             # 1
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],  # 2
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],             # 3
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],  # 4
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 4], [0, 0, 4], [0, 0, 4]],             # 5
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 4], [0, 0, 4], [0, 0, 4], [0, 0, 1]],  # 6
[[0, 0, 0], [0, 0, 0], [0, 0, 4], [0, 0, 4], [0, 0, 1], [0, 0, 1]],             # 7
[[0, 0, 0], [0, 0, 4], [0, 0, 2], [0, 0, 1], [0, 0, 1], [0, 0, 2], [0, 0, 3]],  # 8
[[0, 0, 4], [0, 0, 4], [0, 0, 2], [0, 0, 1], [0, 0, 2], [0, 0, 3]],             # 9
[[0, 0, 1], [0, 0, 2], [0, 0, 2], [0, 0, 2], [0, 0, 3], [0, 0, 2], [0, 0, 2]],  # 10
[[0, 0, 1], [0, 0, 1], [0, 0, 2], [0, 0, 2], [0, 0, 2], [0, 0, 2]],             # 11 (BOTTOM)
]

# test_mat = [
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],  # 0 (TOP)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],             # 1
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],  # 2
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],             # 3
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],  # 4
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],             # 5
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],  # 6
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],             # 7
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],  # 8
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],             # 9
# [[0, 0, 2], [0, 0, 0], [0, 0, 2], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],  # 10
# [[0, 0, 2], [0, 0, 2], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],             # 11 (BOTTOM)
# ]
text = get_stats(test_mat, 0)
"""print(text[0])
print(text[1])
print(text[2])"""