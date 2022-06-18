# Bar Graph Pattern
# Given an integer N, the program must print the pattern as shown in the Example Input/Output section.

# Boundary Condition(s):
# 1 <= N <= 100

# Input Format:
# The first line contains N.
# The second line contains N integers separated by space.

# Output Format:
# The pattern is printed as shown in the Example Input/Output section.

# Example Input/Output 1:
# Input:
# 3
# 2 1 3

# Output:
# --*
# *-*
# ***

# Example Input/Output 2:
# Input:
# 6
# 6 3 2 4 2 1

# Output:
# *-----
# *-----
# *--*--
# **-*--
# *****-
# ******






n=int(input())
arr = list(map(int,input().split()))
max = max(arr)
mat = [['-']*n for _ in range(max)]
for j in range(n):
    for i in range((arr[j])):
        mat[max-i-1][j]='*'
for row in mat:
    print(*row,sep='')