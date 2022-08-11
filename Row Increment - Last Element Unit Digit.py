# Row Increment - Last Element Unit Digit

# The program must accept an integer matrix of size R*C as input. Then the elements in a given row must be incremented by the value of the unit digit of the last element in that specific row. Finally the program must print the revised matrix values.

# Boundary Condition(s):
# 1 <= R, C <= 100

# Input Format:
# The first line contains the value of R and C separated by space(s).
# The next R lines contain C integers separated by space.

# Output Format:
# R lines each containing C integers modified as per the given conditions.

# Example Input/Output 1:
# Input:
# 3 4
# 10 12 13 15
# 23 88 12 42
# 99 89 79 11

# Output:
# 15 17 18 20
# 25 90 14 44
# 100 90 80 12






r,c=map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(r)]
[[[print(row[i]+row[-1]%10,end=' ') for i in range(c)],print()] for row in mat]