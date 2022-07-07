# Distance From Origin
# A point in a graph (x,y) is given as input. The program must print the distance between the given point and the origin with precision up to two decimal places.

# Boundary Condition(s):
# 1 <= x, y <= 100

# Input Format:
# The first line contains the value of x and y separated by space(s).

# Output Format:
# The first line contains the distance with precision up to two decimal places.

# Example Input/Output 1:
# Input:
# 3 3

# Output:
# 4.24

# Example Input/Output 2:
# Input:
# 4 0

# Output:
# 4.00









import math
a,b=map(int,input().split())
print("%.2f" % math.sqrt((a*a)+(b*b)))