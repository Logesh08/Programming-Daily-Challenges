# Number of Changes - ABCD Submatrix
# The program must accept a character matrix of size R*C containing only A, B, C and D as the input. The values of R and C are always even. The program must print the number of changes required in the matrix so that each 2*2 submatrix contains 4 alphabets A, B, C and D in the sorted order.

# Boundary Condition(s):
# 2 <= R, C <= 50

# Input Format:
# The first line contains R and C separated by a space.
# The next R lines, each contains C characters separated by a space.

# Output Format:
# The first line contains an integer value representing the number of changes required in the matrix as per the given condition.

# Example Input/Output 1:
# Input:
# 2 2
# B B
# C D

# Output:
# 1

# Explanation:
# Only change required is in the position (1, 1) B -> A.
# So the matrix becomes
# A B
# C D

# Example Input/Output 2:
# Input:
# 6 4
# C C C A
# C B D B
# C B A B
# B D C D
# D C A B
# B A D D

# Output:
# 14




r,c=map(int,input().split())
mat=[input().split() for _ in range(r)]
count=0
for i in range(0,r,2):
    for j in range(0,c,2):
        if mat[i][j]!="A": count+=1
        if mat[i][j+1]!="B": count+=1
        if mat[i+1][j]!="C": count+=1
        if mat[i+1][j+1]!="D": count+=1
print(count)