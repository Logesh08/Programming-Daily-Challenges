# Inverted Triangle Pattern
# Given an integer N, the program must print the pattern as shown in the Example Input/Output section.

# Boundary Condition(s):
# 1 <= N <= 100

# Input Format:
# The first line contains N.

# Output Format:
# The pattern is printed as shown in the Example Input/Output section.

# Example Input/Output 1:
# Input:
# 4

# Output:
# 1*2*3*4
# *7*6*5*
# **8*9**
# ***10***

# Example Input/Output 2:
# Input:
# 5

# Output:
# 1*2*3*4*5
# *9*8*7*6*
# **10*11*12**
# ***14*13***
# ****15****









p=1
n=int(input())
for i in range(n):
    r = range(p,p+n-i)
    if i%2:
        r = r[::-1]
    print('*'*i,end='')
    l = []
    for x in r:
        l.append(x)
        p+=1
    print(*l,sep='*',end='')
    print('*'*(i))