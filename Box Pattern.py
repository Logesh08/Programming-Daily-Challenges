# Box Pattern

# The program must accept an integer N as the input. The program must print the pattern as shown in the Example Input/Output section.

# Boundary Condition(s):
# 2 <= N <= 15

# Input Format:
# The first line contains the value of N.

# Output Format:
# The list of lines contain the pattern as shown in the Example Input/Output section.

# Example Input/Output 1:
# Input:
# 2

# Output:
# 222
# 212
# 222

# Example Input/Output 2:
# Input:
# 4

# Output:
# 4444444
# 4333334
# 4322234
# 4321234
# 4322234
# 4333334
# 4444444





n = int(input())
mat = [[0]*(2*n - 1) for _ in range(2*n -1)]
for i in range(n):
    for j in range(0+i,len(mat[0])-i):
        mat[j][-i-1] = mat[j][i] = mat[i][j] = mat[-i-1][j] = n - i
for row in mat: print(*row,sep='')