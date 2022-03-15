# First D Surrounding Digits Sum
# The program must accept an integer matrix of size R*C containing only digits from 1 to 8 as the input. For each digit D in the matrix, the program must print the sum of the first D surrounding digits as the output. If the number of surrounding digits of D is less than D, then the program must print the sum of all the surrounding digits of D.

# The order of surrounding digits is given below.
# top-left, top, top-right, right, bottom-right, bottom, bottom-left and left.

# Boundary Condition(s):
# 2 <= R, C <= 50

# Input Format:
# The first line contains R and C separated by a space.
# The next R lines, each contains C integers separated by a space.

# Output Format:
# The first R lines, each contains C integers separated by a space representing the sum of surrounding digits based on the given conditions.

# Example Input/Output 1:
# Input:
# 3 3
# 7 5 2
# 3 8 3
# 2 4 1

# Output:
# 16 23 11
# 20 27 8
# 11 15 8

# Explanation:
# The integer at (1, 1) is 7 -> 5 + 8 + 3 = 16.
# The integer at (1, 2) is 5 -> 7 + 2 + 3 + 8 + 3 = 23.
# The integer at (1, 3) is 2 -> 3 + 8 = 11.
# The integer at (2, 1) is 3 -> 7 + 5 + 8 = 20.
# The integer at (2, 2) is 8 -> 7 + 5 + 2 + 3 + 1 + 4 + 2 + 3 = 27.
# The integer at (2, 3) is 3 -> 5 + 2 + 1 = 8.
# The integer at (3, 1) is 2 -> 3 + 8 = 11.
# The integer at (3, 2) is 4 -> 3 + 8 + 3 + 1 = 15.
# The integer at (3, 3) is 1 -> 8 = 8.
# Hence the output is
# 16 23 11
# 20 27 8
# 11 15 8

# Example Input/Output 2:
# Input:
# 3 4
# 3 4 4 3
# 1 7 1 4
# 3 5 5 2

# Output:
# 12 13 15 9
# 3 25 4 14
# 13 17 19 5






r,c=map(int,input().split()) 
mat = [list ( map(int, input().split() ) ) for _ in range(r)]
x = [-1,-1,-1,0,1,1, 1, 0]
y = [-1, 0, 1,1,1,0,-1,-1]
for i in range(r):
    for j in range(c):
        s = 0
        X = 0
        for _ in range (8):
            if X == mat[i][j]:
                break
            I,J = i+x[_] , j+y[_]
            if 0<= I < r and 0<= J <c:
                s += mat[I][J]
                X += 1
        print(s,end=' ')
    print()