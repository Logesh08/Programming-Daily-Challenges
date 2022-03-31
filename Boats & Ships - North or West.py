# Boats & Ships - North or West
# The program must accept a character matrix of size R*C representing a port as the input. The character asterisk (*) represents water. The character hash symbol (#) represents a boat. Two consecutive hash symbols (vertically or horizontally) represent a ship. The vertical ships can move only towards the north. The horizontal ships can move only towards the west. The boats can move towards north or west. The boats and ships leave the port based on the following conditions.
# - Every odd minute, the first occurring boat or the vertical ship in each column leave the port (towards north).
# - Every even minute, the first occurring boat or the horizontal ship in each row leave the port (towards west).
# - A boat or ship cannot move if there is another boat or ship on its way.
# The program must print the number of minutes it takes to empty the port as the output.

# Boundary Condition(s):
# 2 <= R, C <= 25

# Input Format:
# The first line contains R and C separated by a space.
# The next R lines, each contains C characters separated by a space.

# Output Format:
# The first line contains the number of minutes it takes to empty the port.

# Example Input/Output 1:
# Input:
# 7 6
# # # * # # *
# * * # * * #
# # * # * # *
# * * * * # *
# # * # # * #
# * # * * * *
# * * * * # *

# Output:
# 5

# Explanation:
# After 1 minute (1 vertical ship and 1 boat left the port), the port becomes
# # # * # # *
# * * * * * *
# # * * * # *
# * * * * # *
# # * # # * #
# * # * * * *
# * * * * # *
# After 2 minutes (1 horizontal ship and 4 boats left the port), the port becomes
# * * * # # *
# * * * * * *
# * * * * # *
# * * * * # *
# * * # # * #
# * * * * * *
# * * * * * *
# After 3 minutes (1 boat left the port), the port becomes
# * * * # # *
# * * * * * *
# * * * * # *
# * * * * # *
# * * # # * *
# * * * * * *
# * * * * * *
# After 4 minutes (2 horizontal ships left the port), the port becomes
# * * * * * *
# * * * * * *
# * * * * # *
# * * * * # *
# * * * * * *
# * * * * * *
# * * * * * *
# After 5 minutes (1 vertical ship left the port), the port becomes empty.
# It takes 5 minutes to empty the port. So 5 is printed as the output.

# Example Input/Output 2:
# Input:
# 6 7
# * * * # * # #
# # # * * * * *
# * * # * * # *
# * # * # * # *
# * # * # * * #
# # * # * * # *

# Output:
# 4








r,c = map(int,input().split())
mat = [input().split() for _ in range(r)]
star=0
for i in range(r):
    for j in range(c):
        if mat[i][j] == '*':
            star+=1
            continue
        if mat[i][j]=='#' and j+1<c and mat[i][j+1]=='#':
            mat[i][j] = mat[i][j+1] = 'H'
        elif mat[i][j]=='#' and i+1<r and mat[i+1][j]=='#':
            mat[i][j] = mat[i+1][j] = 'V'
        elif mat[i][j]=='#':
            mat[i][j]='B'
loop = 0
while star != r*c:
    if loop%2==0:
        for j in range(c):
            for i in range(r):
                if mat[i][j] == 'H':
                    break
                elif mat[i][j] == 'V':
                    mat[i][j] = mat[i+1][j] = '*'
                    star+=2
                    break
                elif mat[i][j] == 'B':
                    mat[i][j] = '*'
                    star+=1
                    break
    else:
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 'V':
                    break
                elif mat[i][j] == 'H':
                    mat[i][j] = mat[i][j+1] = '*'
                    star+=2
                    break
                elif mat[i][j] == 'B':
                    mat[i][j] = '*'
                    star+=1
                    break
    loop+=1
print(loop)