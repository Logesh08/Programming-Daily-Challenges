# Pattern Printing - X Pattern with Asterisk

# Accept a number N as the input. The program must print the X pattern as shown in the Example Input/Output Section as the output. (Note: Spaces should be replaced with asterisk)

# Boundary Condition(s):
# 2 <= N <= 50

# Input Format:
# The first line contains the value of N.

# Output Format:
# The list of lines contain the desired pattern.

# Example Input/Output 1:
# Input:
# 4

# Output:
# 1*****1
# *2***2*
# **3*3**
# ***4***
# **3*3**
# *2***2*
# 1*****1

# Example Input/Output 2:
# Input:
# 5

# Output:
# 1*******1
# *2*****2*
# **3***3**
# ***4*4***
# ****5****
# ***4*4***
# **3***3**
# *2*****2*
# 1*******1





n = int(input())
mat = [['*']*(n*2 -1 ) for _ in range(n*2 -1)]
for i in range(n):
    mat[i][i] = mat [i][-i-1] = mat[-i-1][i] = mat[-i-1][-i-1] = i+1
for row in mat:
    print(*row,sep='')