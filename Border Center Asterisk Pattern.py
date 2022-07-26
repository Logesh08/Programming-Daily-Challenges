# Border Center Asterisk Pattern

# Accept an integer N as the input. The program must print the pattern as shown in the Example Input/Output section below. (Note:Integer N is always odd). Asterisk is printed along the border and in the center of the N*N matrix which is printed as the output.

# Boundary Condition(s):
# 1 <= N <= 25

# Input Format:
# The first line contains the value of N.

# Output Format:
# The N lines contain the desired pattern.

# Example Input/Output 1:
# Input:
# 5

# Ouput:
# * * * * *
# * 1 2 3 *
# * 4 * 6 *
# * 7 8 9 *
# * * * * *

# Example Input/Output 2:
# Input:
# 3

# Output:
# * * *
# * * *
# * * *





n = int(input())
arr = [['*']*n for _ in range(n)]
cur = 1
for i in range(1,n - 1):
    for j in range(1, n -1 ):
        arr[i][j] = cur
        cur += 1 
arr[n//2][n//2] = '*'
for row in arr:
    print(*row)