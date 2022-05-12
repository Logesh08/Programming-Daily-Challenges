# Replace Color - Adjacent Pixels
# The program must accept a character matrix of size R*C representing an image, the location of a pixel in the image (X, Y) and a color CH as the input. The program must replace the color of the given pixel and all adjacent same colored pixels with the color CH (all 8 possible directions). Finally, the program must print the revised matrix as the output.

# Boundary Condition(s):
# 2 <= R, C <= 50
# 1 <= X <= R
# 1 <= Y <= C

# Input Format:
# The first line contains R and C separated by a space.
# The next R lines, each contains C characters separated by a space.
# The R+2nd contains X, Y and CH separated by a space.

# Output Format:
# The first R lines contain the revised matrix.

# Example Input/Output 1:
# Input:
# 4 3
# B B W
# W W W
# W W W
# B B B
# 2 2 G

# Output:
# B B G
# G G G
# G G G
# B B B

# Explanation:
# Here R = 4, C = 3, X = 2, Y = 2 and CH = G.
# After replacing the color of the given pixel and all the adjacent same colored pixels with the color G, the image becomes
# B B G
# G G G
# G G G
# B B B

# Example Input/Output 2:
# Input:
# 5 6
# R G R Y Y Y
# G R G Y R R
# R R R Y R R
# G R G Y Y Y
# G R R R G G
# 4 2 P

# Output:
# P G P Y Y Y
# G P G Y R R
# P P P Y R R
# G P G Y Y Y
# G P P P G G











r,c = map(int,input().split())
mat = [input().split() for _ in range(r)]
x,y,color = input().split()
def INT(X): return int(X)-1
x,y = map(INT,[x,y])
itr = [-1,0,1]
cur = mat[x][y]
def spreadColor(x,y):
    for i in itr:
        i+=x
        for j in itr:
            j+=y
            if 0<= i < r and 0<= j < c:
                if mat[i][j] == cur:
                    mat[i][j] = color
                    spreadColor(i,j)
spreadColor(x,y)
for row in mat: 
    print(*row)