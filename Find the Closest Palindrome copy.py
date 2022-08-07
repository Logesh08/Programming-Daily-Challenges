# Find the Closest Palindrome

# The program must accept a number N as the input. The program must print the closest palindromic number as the output. If there are two closest palindromic numbers the program must print the smaller number.

# Boundary Condition(s):
# 2 <= N <= 99999999999999

# Input Format:
# The first line contains the value of N.

# Output Format:
# The first line contains the closest palindromic number.

# Example Input/Output 1:
# Input:
# 124

# Output:
# 121

# Example Input/Output 2:
# Input:
# 1439

# Output:
# 1441









N=input().strip();X=N
while(N!=N[::-1] and X!=X[::-1]):
    N=str(int(N)+1)
    X=str(int(X)-1)
if(X==X[::-1]):
    print(X)
else:
    print(N)