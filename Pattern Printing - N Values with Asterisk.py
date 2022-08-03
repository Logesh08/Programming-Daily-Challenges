# Pattern Printing - N Values with Asterisk

# Accept an integer N as the input. The program must print the pattern as shown in the Example Input/Output section below.

# Boundary Condition(s):
# 1 <= N <= 50

# Input Format:
# The first line contains the value of N.

# Output Format:
# The first three lines contain the desired pattern.

# Example Input/Output 1:
# Input:
# 3

# Output:
# *******
# *1*2*3*
# *******

# Example Input/Output 2:
# Input:
# 5

# Output:
# ***********
# *1*2*3*4*5*
# ***********







n = int(input())
print('*'*(n*2 + 1))
print('*'+'*'.join([str(i+1) for i in range(n)])+'*')
print('*'*(n*2 + 1))


# OneLiner
(lambda x: print('*'*(x*2+1),'*'+'*'.join([str(i+1) for i in range(x)])+'*','*'*(x*2+1),sep='\n'))(int(input()))