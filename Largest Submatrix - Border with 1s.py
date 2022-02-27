# Largest Submatrix - Border with 1s
# The program must accept an integer matrix of size R*C containing only 0s and 1s as the input. The program must print the size of the largest square submatrix of the minimum size 2 where all the elements in the border are 1s. If there is no such submatrix, then the program must print -1 as the output.

# Boundary Condition(s):
# 2 <= R, C <= 50

# Input Format:
# The first line contains R and C separated by a space.
# The next R lines, each contains C integer values separated by a space.

# Output Format:
# The first line contains an integer value representing the size of the largest square submatrix or -1 based on the given conditions.

# Example Input/Output 1:
# Input:
# 6 8
# 0 0 0 0 0 1 1 0
# 1 1 1 0 0 0 0 0
# 0 0 1 1 1 1 1 1
# 1 1 1 1 0 1 1 0
# 1 1 0 1 0 1 1 0
# 0 0 0 1 1 1 1 1

# Output:
# 4

# Explanation:
# The largest square submatrix of size 4*4 with 1s in the border is highlighted below.
# 0 0 0 0 0 1 1 0
# 1 1 1 0 0 0 0 0
# 0 0 1 1 1 1 1 1
# 1 1 1 1 0 1 1 0
# 1 1 0 1 0 1 1 0
# 0 0 0 1 1 1 1 1

# Example Input/Output 2:
# Input:
# 4 3
# 1 1 0
# 1 0 1
# 0 1 1
# 1 1 0

# Output:
# -1




rows,cols = map(int, input().split())
grid= [ list ( map ( int , input() .split())) for i in range(rows)] 
# rows, cols = len(grid), len(grid[0])
answer = 0 
def checkzero(i,j,side):
    if 0 in grid[i][j:j+side] or 0 in grid[i+side-1][j:j+side]:
      return True
    for x in range(i,i+side):
      if grid[x][j] == 0 or grid[x][j+side-1] == 0:
        return True
    return False

for side in range(1, min(rows,cols) + 1):
    for i in range(rows):
      for j in range(cols):
        if i+side > rows or j + side > cols:
          continue
        if checkzero(i,j,side) == False:
          answer = max(answer, side)
if answer==1: answer=-1      
print(answer) 
