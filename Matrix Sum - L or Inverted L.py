# Matrix Sum - L or Inverted L
# The program must accept an integer matrix of size N*N as the input. The program must find the sum of integers in the L-shape and inverted L-shape of the matrix. If the sum of the integers in L-shape and the sum of the integers in inverted L-shape are equal then print YES as the output. Else the program must print NO as the output.

# Boundary Condition(s):
# 3 <= N <= 50
# 1 <= Matrix element value <= 1000

# Input Format:
# The first line contains N.
# The next N lines each contain N integers separated by a space.

# Output Format:
# The first line contains either YES or NO.

# Example Input/Output 1:
# Input:
# 4
# 1 6 3 4
# 2 3 4 2
# 3 4 5 5
# 4 5 6 7

# Output:
# YES

# Explanation:
# The integers in the L-shape are highlighted below.
# 1 6 5 4
# 2 3 4 2
# 3 4 5 3
# 4 5 6 7
# The integers in the inverted L-shape are highlighted below.
# 1 6 5 4
# 2 3 4 2
# 3 4 5 3
# 4 5 6 7
# The sum of integers in the L-shape (1+2+3+4+5+6+7) is 28.
# The sum of integers in the inverted L-shape (1+6+5+4+2+3+7) is 28.
# Both the sum values are equal. So YES is printed.

# Example Input/Output 2:
# Input:
# 5
# 7 27 20 60 67
# 82 77 12 74 32
# 98 14 62 1 77
# 45 11 55 6 92
# 27 30 30 27 8

# Output:
# NO

# Example Input/Output 3:
# Input:
# 7
# 5 4 8 4 2 6 2
# 2 9 7 1 1 2 3
# 1 3 2 7 2 3 3
# 2 3 8 6 7 9 8
# 6 4 5 1 4 2 1
# 8 2 9 3 2 1 3
# 7 4 2 5 4 3 7

# Output:
# YES









n = int(input())
mat = [list(map(int,input().split())) for _ in range(n)]
imat = list(map(list,zip(*mat)))
if (sum(imat[0])+sum(mat[-1][1:])) == (sum(mat[0][:-1])+sum(imat[-1])):
    print('YES')
else:
    print('NO')