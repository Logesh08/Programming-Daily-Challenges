# Check if Vertical Zig-Zag or Not

# The program must accept an integer matrix with size NxN as input. The program must print "Yes" if the given matrix is vertically zig-zag. Else the program must print "No" as the output.
# Note: The matrix must be filled with first N*N natural numbers starting from 1 in vertical zig-zag fashion.

# Boundary Condition(s):
# 1 <= N <= 50
# 0 <= Matrix Elements <= 999

# Input Format:
# The first line contains the value of N.
# The next N lines contain N integers separated by space(s).

# Output Format:
# The first line contains either "Yes" or "No".

# Example Input/Output 1:
# Input:
# 5
# 1 10 11 20 21
# 2 9 12 19 22
# 3 8 13 18 23
# 4 7 14 17 24
# 5 6 15 16 25

# Output:
# Yes

# Example Input/Output 2:
# Input:
# 3
# 1 2 3
# 4 5 6
# 7 8 9

# Output:
# No






n = int(input())
mat = [list(map(int,input().split())) for _ in range(n)]
start = 1
flag = True
for j in range(n):
    r = range(n)
    if j%2:
        r = r[::-1]
    for i in r:
        if mat[i][j]==start:
            start+=1 
        else:
            flag=False
            break 
print('Yes' if flag else 'No')