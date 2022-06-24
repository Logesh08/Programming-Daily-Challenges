# Right Angled Triangle Check
# Three sides of a triangle are passed as input. The program must print yes if the sides form a right angled triangle. Else the program must print no.

# Boundary Condition(s):
# 1 <= Length of the sides <= 999999999

# Input Format:
# The first line contains three integers denoting the length of the sides separated by a space.

# Output Format:
# The first line contains yes or no

# Example Input/Output 1:
# Input:
# 5 4 3

# Output:
# yes

# Example Input/Output 2:
# Input:
# 8 5 6

# Output:
# no








sides = list(map(int,input().split()))
sides.sort()
if (sides[0]*sides[0])+(sides[1]*sides[1]) == sides[2]*sides[2]:
    print('yes')
else:
    print('no')