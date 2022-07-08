# Greater Values in Array
# An array of N integers and an integer value M are given as input. The program must print all the values which are greater than M in the array.

# Boundary Condition(s):
# 1 <= N <= 1000

# Input Format:
# The first line contains the value of N and M separated by space(s).
# The second line contains N integers separated by space(s).

# Output Format:
# The first line contains the integers greater than M separated by a space.

# Example Input/Output 1:
# Input:
# 6 4
# 1 4 6 2 9 1

# Output:
# 6 9

# Example Input/Output 2:
# Input:
# 8 45
# 21 46 78 16 40 56 89 35

# Output:
# 46 78 56 89







n,m=map(int,input().split())
print(*[i for i in input().split() if int(i)>m])




### One Liner
