# Matrix - Sort Odd Integers
# The program must accept an integer matrix of size R*C. Then the program must sort the odd integers in the matrix across all rows. Finally, the program must print the revised matrix.

# Boundary Condition(s):
# 2 <= R, C <= 50
# 1 <= Matrix element value <= 10^4

# Input Format:
# The first line contains R and C separated by a space.
# The next R lines, each contains C integer values separated by a space.

# Output Format:
# The first R lines contain the revised matrix.

# Example Input/Output 1:
# Input:
# 3 4
# 90 5 85 29
# 53 9 17 88
# 16 99 41 21

# Output:
# 90 5 9 17
# 21 29 41 88
# 16 53 85 99

# Explanation:
# Here R=3 and C=4.
# The odd integers in the given 3*4 matrix are highlighted below.
# 90 5 85 29
# 53 9 17 88
# 16 99 41 21
# After sorting the odd integers in the given matrix, the matrix becomes
# 90 5 9 17
# 21 29 41 88
# 16 53 85 99

# Example Input/Output 2:
# Input:
# 5 7
# 644 74 347 76 782 172 783
# 739 281 601 600 30 431 608
# 437 778 199 396 253 352 687
# 799 648 101 583 542 42 997
# 58 667 581 597 499 579 933

# Output:
# 644 74 101 76 782 172 199
# 253 281 347 600 30 431 608
# 437 778 499 396 579 352 581
# 583 648 597 601 542 42 667
# 58 687 739 783 799 933 997




r,c=map(int,input().split())
mat=[list(map(int,input().split())) for _ in range(r)]
temp=[]
for row in range(r):
    for col in range(c):
        if mat[row][col] % 2:
            temp.append(mat[row][col])
temp.sort()
for row in mat:
    for i in range(c):
        if row[i]%2:
            row[i]=temp.pop(0)
    print(*row)
