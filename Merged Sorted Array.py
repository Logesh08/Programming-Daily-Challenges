# Merged Sorted Array

# The program must accept two sorted arrays of size M and N as input. The program must print the merged sorted array as the output.

# Boundary Condition(s):
# 1 <= M, N <= 20

# Input Format:
# The first line contains the value of M and N separated by space.
# The second line contains the M elements separated by space(s).
# The third line contains the N elements separated by space(s).

# Output Format:
# The first line contains the merged sorted array separated by space(s).

# Example Input/Output 1:
# Input:
# 4 3
# 9 7 7 4
# 7 6 3

# Output:
# 9 7 7 7 6 4 3

# Example Input/Output 2:
# Input:
# 5 4
# 12 11 10 9 8
# 8 7 6 5

# Output :
# 12 11 10 9 8 8 7 6 5





input()
print(*sorted(list(map(int,(input()+input()).split())),reverse=True))