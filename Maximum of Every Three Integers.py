# Maximum of Every Three Integers
# An array of N integers is given as input. The program must print the maximum of every three integers. Assume N is always divisible by three.

# Boundary Condition(s):
# 1 <= N <= 10000

# Input Format:
# The first line contains the value of N.
# The second line contains N integers separated by space.

# Output Format:
# The first line contains N/3 integers separated by a space.

# Example Input/Output 1:
# Input:
# 6
# 23 67 18 5 23 32

# Output:
# 67 32

# Example Input/Output 2:
# Input:
# 9
# 22 24 67 60 93 96 102 23 56

# Output:
# 67 96 102









n=int(input())
arr = list(map(int,input().split()))
for i in range(0,n,3):
    print(max(arr[i:i+3]),end=' ')