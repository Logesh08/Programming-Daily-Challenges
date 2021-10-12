# Kth Border Pattern
# The program must accept two integers N and K as the input. The program must form a grid of asterisks of size N*N. Then the program must replace the asterisks in the Kth border of the grid with the hash symbols(#). Finally, the program must print the N*N grid as the output.

# Boundary Condition(s):
# 2 <= N <= 100
# 1 <= K <= (N+1)/2

# Input Format:
# The first line contains N and K separated by a space.

# Output Format:
# The first N lines, each contains N characters separated by a space.

# Example Input/Output 1:
# Input:
# 5 1

# Output:
# # # # # #
# # * * * #
# # * * * #
# # * * * #
# # # # # #

# Explanation:
# Here N=5, so the 5*5 grid of asterisks is formed.
# The value of K is 1, so the 1st border is replaced with the hash symbols.
# Now the 5*5 grid becomes
# # # # # #
# # * * * #
# # * * * #
# # * * * #
# # # # # #

# Example Input/Output 2:
# Input:
# 6 3

# Output:
# * * * * * *
# * * * * * *
# * * # # * *
# * * # # * *
# * * * * * *
# * * * * * *

# Example Input/Output 3:
# Input:
# 7 2

# Output:
# * * * * * * *
# * # # # # # *
# * # * * * # *
# * # * * * # *
# * # * * * # *
# * # # # # # *
# * * * * * * *






n,k=map(int,input().split())
matrix=[['*' for i in range(n)]for j in range(n)]
for i in range(k-1,n-k+1):
    matrix[k-1][i]='#'
    matrix[i][n-k]='#'
    matrix[n-k][i]='#'
    matrix[i][k-1]='#'
for i in matrix:
    print(*i)