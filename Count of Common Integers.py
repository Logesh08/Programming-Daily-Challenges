# Count of Common Integers

# The program must accept an integer matrix of size NxN as input. The program must print the count of common integers between top right and bottom left submatrices of the given matrix. 

# Boundary Condition(s):
# 2 <= N <= 50

# Input Format:
# The first line contains the value of N.
# The next N lines contain N integers each separated by space.

# Output Format:
# The first line contains the count of common integers between top right and bottom left of the matrix.

# Example Input/Output 1:
# Input:
# 5
# 1 2 3 4 2
# 6 7 8 9 0
# 1 2 3 4 5
# 6 7 8 9 0
# 9 2 3 4 5 

# Output:
# 5

# Explanation:
# The top right submatrix elements of the given matrix are 3 4 2 8 9 0 3 4 5.
# The bottom left submatrix elements of the given matrix are 1 2 3 6 7 8 9 2 3.
# The common integers between top right and bottom left submatrices of the given matrix are 2 3 3 8 and 9.
# Hence, the count 5 is printed as the output.

# Example Input/Output 2:
# Input:
# 4
# 12 23 34 45
# 23 34 12 56
# 34 45 56 67
# 12 23 34 45

# Output:
# 3









n  =int(input())
arr = [input().split() for _ in range(n)]
a ,b = [],[]
n//=2
for i in range(n+1):
    for j in range(n+1):
        a.append(arr[i][j+n])
        b.append(arr[i+n][j])
count = 0
for i in set(a):
    if i in set(b):
        count += min([a.count(i),b.count(i)])
print(count)