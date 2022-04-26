# Interlace Odd Even Matrix Pattern
# The program must accept an integer N as the input. The program must print an integer matrix of size N*N containing with the odd and even integers alternately among the integers from 1 to N*N as shown in the Example Input/Output section.

# Boundary Condition(s):
# 1 <= N <= 100

# Input Format:
# The first line contains N.

# Output Format:
# The first N lines, each contains N integers separated by a space representing the N*N matrix.

# Example Input/Output 1:
# Input:
# 3

# Output:
# 1 8 3
# 6 5 4
# 7 2 9

# Explanation:
# Here N = 3.
# The integers from 1 to 3*3 are 1, 2, 3, 4, 5, 6, 7, 8, 9.
# So the 3*3 matrix is formed as given below.
# 1 8 3
# 6 5 4
# 7 2 9

# Example Input/Output 2:
# Input:
# 4

# Output:
# 1 16 3 14
# 5 12 7 10
# 9 8 11 6
# 13 4 15 2

# Example Input/Output 3:
# Input:
# 5

# Output:
# 1 24 3 22 5
# 20 7 18 9 16
# 11 14 13 12 15
# 10 17 8 19 6
# 21 4 23 2 25








a=1
b=int(input())
r = b
b *= b
i=a;j=b
count = 0
while(i<=b and j>=a):
    if i%2!=0:
        print(i,end=" ")
    i+=1
    if j%2==0:
        print(j,end=" ")
    j-=1 
    count+=1 
    if count%r==0:
        print()
