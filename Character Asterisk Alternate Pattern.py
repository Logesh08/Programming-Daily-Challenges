# Character Asterisk Alternate Pattern

# An integer N is passed as the input. The program must print the pattern as given in the Example Input/Output Section.

# Boundary Condition(s):
# 2 <= N <= 100

# Input Format:
# The first line contains N.

# Output Format:
# The first N lines contain the pattern.

# Example Input/Output 1:
# Input:
# 3

# Output:
# a*b*c
# *d*e*
# f*g*h

# Example Input/Output 2:
# Input:
# 4

# Output:
# a*b*c*d
# *e*f*g*
# h*i*j*k
# *l*m*n*








n = int(input())
c = ord('a')
for i in range(n):
    if i%2: print(end='*')
    for j in range(n - (i%2)):
        print(chr(c),end='')
        if i%2 or (i%2==0 and j!=n-1): print(end='*')
        c += 1
        if c > ord('z'): c = 97
    print()