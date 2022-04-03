# Append Alphabet - Surrounding Integers
# The program must accept a matrix of size R*C containing integers and alphabets as the input. For each occurrence of the alphabet in the matrix, the program must append the alphabet to the surrounding integers of the alphabet. Then the program must print the revised matrix as the output.
# Note: In the given matrix, there are no common integers around two or more alphabets.

# Boundary Condition(s):
# 2 <= R, C <= 50
# 1 <= Each integer value in the matrix <= 1000

# Input Format:
# The first line contains R and C separated by a space.
# The next R lines, each contains C elements of the matrix separated by a space.

# Output Format:
# The first R lines contain the revised matrix.

# Example Input/Output 1:
# Input:
# 4 5
# 5 2 2 2 4
# 7 5 2 3 b
# 8 a 5 5 9
# 9 3 8 5 6

# Output:
# 5 2 2 2b 4b
# 7a 5a 2a 3b b
# 8a a 5a 5b 9b
# 9a 3a 8a 5 6

# Explanation:
# Here R=4 and C=5.
# The alphabets in the given matrix are highlighted below
# 5 2 2 2 4
# 7 5 2 3 b
# 8 a 5 5 9
# 9 3 8 5 6
# After modifying the matrix based on the given conditions, the matrix becomes
# 5 2 2 2b 4b
# 7a 5a 2a 3b b
# 8a a 5a 5b 9b
# 9a 3a 8a 5 6

# Example Input/Output 2:
# Input:
# 5 5
# 86 77 45 57 82
# 13 A 10 86 70
# 32 74 72 27 C
# 28 79 12 43 90
# 15 B 13 15 37

# Output:
# 86A 77A 45A 57 82
# 13A A 10A 86C 70C
# 32A 74A 72A 27C C
# 28B 79B 12B 43C 90C
# 15B B 13B 15 37








r , c = map(int,input().split())
mat = [input().split() for _ in range(r)]
for i in range(r):
    for j in range(c):
        C=mat[i][j]
        if C.isalpha():
            for x in range(-1,2):
                for y in range(-1,2):
                    if 0 <= x+i < r and 0<= y+j < c:
                        mat[i+x][j+y]+=C
            mat[i][j]=C
for row in mat: print(*row)