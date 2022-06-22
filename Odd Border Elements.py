# Odd Border Elements
# Given an integer N value which is the size of a square matrix, the program must print odd integers present in the border of the square matrix.

# Boundary Condition(s):
# 1 <= N <= 100

# Input Format:
# The first line contains the value of N.
# The next N lines contain the matrix.

# Output Format:
# The first line contains the odd integers present in the border of the matrix each separated by a space.

# Example Input/Output 1:
# Input:
# 3
# 45 87 190
# 74 21 35
# 89 45 42

# Output:
# 45 87 35 89 45

# Example Input/Output 2:
# Input:
# 4
# 56 78 12 30
# 90 56 27 29
# 65 278 25 9
# 37 81 77 20

# Output:
# 29 65 9 37 81 77






n = int(input())
mat = [input().split() for _ in range(n)]
def printer(row):
    for i in row:
        if int(i)%2:
            print(i,end=' ')
printer(mat[0])
for i in range(1,n-1):
    printer([mat[i][0],mat[i][-1]])
printer(mat[-1])