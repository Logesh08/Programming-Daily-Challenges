# Matrix - Integers & Operators
# The program must accept a matrix of size R*C containing integers and operators(+ and -) as the input. For each occurrence of plus(+) in the matrix, the program must replace the operator with the sum of integers on the top and bottom of the operator. Similarly, for each occurrence of minus(-) in the matrix, the program must replace the operator with the absolute difference between the integers on the top and bottom of the operator. Finally, the program must print the revised matrix as the output.

# Note:
# - There will be no consecutive operators in each column of the matrix.
# - There will be no operators on the top and bottom edges of the matrix.

# Boundary Condition(s):
# 3 <= R, C <= 25
# 1 <= Matrix element value <= 10^5

# Input Format:
# The first line contains R and C.
# The next R lines contain the matrix.

# Output Format:
# The first R lines, each contains C integers separated by a space representing the revised matrix.

# Example Input/Output 1:
# Input:
# 4 3
# 10 30 60
# + - 70
# 20 95 +
# 25 50 10

# Output:
# 10 30 60
# 30 65 70
# 20 95 80
# 25 50 10

# Explanation:
# 1st operator is +, so it is replaced with the sum of 10 and 20.
# 2nd operator is -, so it is replaced with the absolute difference between 30 and 95.
# 3rd operator is +, so it is replaced with the sum of 70 and 10.
# Now the matrix becomes
# 10 30 60
# 30 65 70
# 20 95 80
# 25 50 10

# Example Input/Output 2:
# Input:
# 6 6
# 6 7 3 8 3 7
# - 3 9 + 5 1
# 6 - 9 5 - -
# 4 6 3 + 4 3
# - + 9 7 + +
# 1 5 7 6 3 7

# Output:
# 6 7 3 8 3 7
# 0 3 9 13 5 1
# 6 3 9 5 1 2
# 4 6 3 12 4 3
# 3 11 9 7 7 10
# 1 5 7 6 3 7




r,c=map(int,input().split())
mat=[input().split() for i in range(r)]
for i in range(r):
    for j in range(c):
        if mat[i][j] in "+-":
            mat[i][j]=abs(eval(mat[i-1][j]+mat[i][j]+mat[i+1][j]))
    print(*mat[i])