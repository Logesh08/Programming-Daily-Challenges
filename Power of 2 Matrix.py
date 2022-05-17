# Power of 2 Matrix
# The program must accept an integer N as the input. The program must form an integer matrix of size (2^N)*(2^N). The program must fill the matrix with the integers submatrix by submatrix of size 2*2 in the order (Top-left, Top-right, Bottom-left and Bottom-right) as shown in the Example Input/Output section.

# Boundary Condition(s):
# 1 <= N <= 7

# Input Format:
# The first line contains N.

# Output Format:
# The first 2^N lines contain the integer matrix as shown in the Example Input/Output section.

# Example Input/Output 1:
# Input:
# 3

# Output:
# 1 2 5 6 17 18 21 22
# 3 4 7 8 19 20 23 24
# 9 10 13 14 25 26 29 30
# 11 12 15 16 27 28 31 32
# 33 34 37 38 49 50 53 54
# 35 36 39 40 51 52 55 56
# 41 42 45 46 57 58 61 62
# 43 44 47 48 59 60 63 64

# Explanation:
# Here N=3, so the size of the matrix is 8*8 (2^3 * 2^3).
# In the 8*8 matrix, the integer 0 represents the cell is empty.
# 2^1 = 2, so fill the 2*2 matrix with the integers in the order Top-left, Top-right, Bottom-left and Bottom-right.
# 1 2 0 0 0 0 0 0
# 3 4 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 2^2 = 4, so fill the 4*4 matrix with the integers in the order Top-left, Top-right, Bottom-left and Bottom-right.
# 1 2 5 6 0 0 0 0
# 3 4 7 8 0 0 0 0
# 9 10 13 14 0 0 0 0
# 11 12 15 16 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 2^3 = 8, so fill the 8*8 matrix with the integers in the order Top-left, Top-right, Bottom-left and Bottom-right.
# 1 2 5 6 17 18 21 22
# 3 4 7 8 19 20 23 24
# 9 10 13 14 25 26 29 30
# 11 12 15 16 27 28 31 32
# 33 34 37 38 49 50 53 54
# 35 36 39 40 51 52 55 56
# 41 42 45 46 57 58 61 62
# 43 44 47 48 59 60 63 64

# Example Input/Output 2:
# Input:
# 2

# Output:
# 1 2 5 6
# 3 4 7 8
# 9 10 13 14
# 11 12 15 16

# Example Input/Output 3:
# Input:
# 1

# Output:
# 1 2
# 3 4










x=int(input())
n=2**x
matrix=[[0 for i in range(n)]for j in range(n)]
x=1
n//=2
def fill(size,i,j):
    global x
    if size==1:
        matrix[i][j]=x
        x+=1
        return
    else:
        size//=2
        fill(size,i,j)
        fill(size,i,j+size)
        fill(size,i+size,j)
        fill(size,i+size,j+size)
fill(n,0,0)
fill(n,0,n)
fill(n,n,0)
fill(n,n,n)
for i in matrix:
    print(*i)






## 2
