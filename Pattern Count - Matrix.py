# Pattern Count - Matrix
# The program must accept an integer matrix of size R*C containing only 0s and 1s as the input. The program must print the number of occurrences of the following pattern in the given matrix.
# 1 0 1
# 0 1 0
# 1 0 1

# Boundary Condition(s):
# 3 <= R, C <= 50

# Input Format:
# The first line contains R and C separated by a space.
# The next R lines, each contains C integer values separated by a space.

# Output Format:
# The first line contains an integer value representing the number of occurrences of the given pattern in the matrix.

# Example Input/Output 1:
# Input:
# 5 6
# 0 0 1 1 0 0
# 0 1 0 1 0 1
# 0 0 1 0 1 0
# 1 1 0 1 0 1
# 0 0 1 0 1 1

# Output:
# 3

# Explanation:
# Here R=5 and C=6.
# The first occurrence of the pattern is highlighted below.
# 0 0 1 1 0 0
# 0 1 0 1 0 1
# 0 0 1 0 1 0
# 1 1 0 1 0 1
# 0 0 1 0 1 1

# The second occurrence of the pattern is highlighted below.
# 0 0 1 1 0 0
# 0 1 0 1 0 1
# 0 0 1 0 1 0
# 1 1 0 1 0 1
# 0 0 1 0 1 1

# The third occurrence of the pattern is highlighted below.
# 0 0 1 1 0 0
# 0 1 0 1 0 1
# 0 0 1 0 1 0
# 1 1 0 1 0 1
# 0 0 1 0 1 1

# There are 3 occurrences of the given pattern in the matrix, so 3 is printed as the output.

# Example Input/Output 2:
# Input:
# 4 3
# 0 1 0
# 1 0 1
# 0 1 0
# 1 1 1

# Output:
# 0




r,c=map(int ,input().split()) 
mat=[input().split() for _ in range(r)] 
count=0
for i in range(r):
    for j in range(c):
        x,y=i,j
        if 0 <= x+2 < r and 0<= y+2 < c:
            if mat[x][y] == "1" and mat[x][y+1]=="0"  and mat[x][y+2]=="1"  and mat[x+1][y]=="0"  and mat[x+1][y+1]=="1"  and mat[x+1][y+2]=="0"  and mat[x+2][y]=="1"  and mat[x+2][y+1]=="0" and mat[x+2][y+2]=="1":
                count+=1 
print(count) 
