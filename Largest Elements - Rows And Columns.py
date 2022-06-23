# Largest Elements - Rows And Columns
# Given a  matrix of size N*N as input, the program must print the largest integer of each row and of each column.

# Boundary Condition(s):
# 2 <= N <= 50

# Input Format:
# The first line contains the value of N.
# The next N lines contain the elements of the matrix.

# Output Format:
# The first line contains the largest element of each row separated by space.
# The second line contains the largest element of each column separated by space.

# Example Input/Output 1:
# Input:
# 3
# 1 2 3
# 4 5 6
# 7 8 9

# Output:
# 3 6 9 
# 7 8 9 

# Example Input/Output 2:
# Input:
# 4
# 3 5 8 9
# 5 2 4 8
# 5 1 3 4
# 0 1 2 3

# Output:
# 9 8 5 3 
# 5 5 8 9







n = int(input())
mat = [list(map(int,input().split())) for _ in range(n)]
for row in mat:
    print(max(row),end=' ')
print()
for col in list(map(list,zip(*mat))):
    print(max(col),end=' ')