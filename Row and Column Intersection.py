# Row and Column Intersection
# The program must accept an integer matrix of size N*N containing only 0s and 1s as the input.
# The program must find the value of X where X represents the position of a row and column in the matrix which contain 0s in the Xth row and 1s in the Xth column,
# expect the cell (X, X). Then the program must print the value of X as the output. If there is no such row and column, then the program must print -1 as the output.

# Boundary Condition(s):
# 2 <= N <= 50

# Input Format:
# The first line contains N.
# The next N lines contain an integer matrix of size N*N.

# Output Format:
# The first line contains the value of X or the first line contains -1.

# Example Input/Output 1:
# Input:
# 5
# 0 1 1 1 0
# 1 0 1 0 0
# 0 0 1 0 0
# 1 0 1 0 1
# 0 1 1 0 0

# Output:
# 3

# Explanation:
# In the given 5*5 matrix, 3rd row contains 0s and 3rd column contains 1s, except the cell (3, 3).
# So 3 is printed as the output.

# Example Input/Output 2:
# Input:
# 4
# 1 1 0 0
# 0 0 0 0
# 1 1 0 1
# 0 1 1 1

# Output:
# 2

# Example Input/Output 3:
# Input:
# 6
# 1 1 1 1 1 1
# 0 1 1 0 0 0
# 1 1 0 0 1 0
# 0 1 0 0 0 0
# 0 1 0 1 1 0
# 0 1 0 1 1 0

# Output:
# -1



n=int(input())
mat=[input().split() for _ in range(n)]
inversed=list(map(list,zip(*mat)))
for i in range(n):
    mat[i][i]="0"
    inversed[i][i]="1"
    if "1" not in mat[i] and "0" not in inversed[i]:
        print(i+1)
        exit()
print(-1)
