# Concatenate Four Corner Submatrices
# The program must accept a character matrix of size R*C and an integer K as the input. 
# The values of R and C are always not equal. The program must expand the given matrix to a smallest possible square matrix by filling the empty cells with asterisks.
# Then the program must print the concatenated representation of all the four corner square submatrices of size K*K as shown in the Example Input/Output section.
# The order of four corner square submatrices is given below.
# Top-Left, Top-Right, Bottom-Left and Bottom-Right.

# Boundary Condition(s):
# 2 <= R, C <= 50
# 2 <= K <= Maximum value between R and C

# Input Format:
# The first line contains R and C separated by a space.
# The next R lines, each contains C characters separated by a space.
# The R+2nd line contains K.

# Output Format:
# The first K lines, each contains K string values separated by a space representing the concatenated four K*K corner submatrices.

# Example Input/Output 1:
# Input:
# 3 5
# P S g P q
# k b S a K
# k h Z s J
# 2

# Output:
# PP** Sq**
# ka** bK**

# Explanation:
# The given 3*5 matrix is
# P S g P q
# k b S a K
# k h Z s J
# After expanding the given matrix to a smallest possible square matrix of size 5*5, the matrix becomes
# P S g P q
# k b S a K
# k h Z s J
# * * * * *
# * * * * *
# All the 4 corner submatrices of size 2*2 are highlighted below.
# P S g P q
# k b S a K
# k h Z s J
# * * * * *
# * * * * *
# Concatenate the characters present in the same cell in all the 4 corner submatrices as shown below.
# (1, 1) -> P+P+*+* -> PP**
# (1, 2) -> S+q+*+* -> Sq**
# (2, 1) -> k+a+*+* -> ka**
# (2, 2) -> b+K+*+* -> bK**
# So the concatenated representation of all four corner square submatrices of size 2*2 is given below.
# PP** Sq**
# ka** bK**

# Example Input/Output 2:
# Input:
# 6 4
# h L E W
# Y z J j
# w m q O
# w y g A
# I p s e
# F O Z p
# 3

# Output:
# hWwA L*y* E*g*
# YjIe z*p* J*s*
# wOFp m*O* q*Z*

# Example Input/Output 3:
# Input:
# 4 5
# b h k S K
# W f k w T
# D t y C Z
# L r X D G
# 3

# Output:
# bkDy hStC kKyZ
# WkLX fwrD kTXG
# Dy** tC** yZ**




r,c = map(int,input().split())
if r>c: m=r 
else: m=c
mat = [['*']*m for _ in range(m)]
for i in range(r):
    cur = input().split()
    for j in range(c):
        mat[i][j] = cur[j]
k = int(input())
qi=qj = 0
pi , pj = 0,m-k
zi,zj = m-k,0
mi,mj = m-k,m-k
for i in range(k):
    for j in range(k):
        print(mat[qi+i][qj+j],mat[pi+i][pj+j],mat[i+zi][j+zj],mat[mi+i][mj+j],sep='',end=' ')
    print()