# Matrix - Sum of Edge Elements
# The input elements of R*C matrix is passed as the input (R is the number of rows and C is the number of columns in the matrix. The program must print the sum S of the elements along the edge of the matrix.

# Input Format:
# The first line contains R and C separated by a space..
# Next R lines contain C values each, with the values separated by a space.

# Output Format:
# The first line contains S.

# Boundary Conditions:
# 2 <= R, C <= 100
# 1 <= Matrix Cell Value <= 1000

# Example Input/Output 1:
# Input:
# 5 3
# 1 2 3
# 4 5 6
# 7 8 9
# 5 5 5
# 2 2 2

# Output:
# 48

# Example Input/Output 2:
# Input:
# 3 3
# 100 200 300
# 400 500 600
# 700 800 900

# Output:
# 4000






r,c = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(r)]
ans = 0
ans += sum(mat[0][1:-1]) + sum(mat[-1])
mat = list(map(list,zip(*mat)))
ans += sum(mat[0][:-1]) + sum(mat[-1][:-1])
print(ans)