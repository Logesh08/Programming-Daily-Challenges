# Alternate Rows Triangle Pattern
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
# ---1
# --3-2
# -4-5-6
# 10-9-8-7

# Example Input/Output 2:
# Input:
# 5

# Output:
# ----1
# ---3-2
# --4-5-6
# -10-9-8-7
# 11-12-13-14-15












n = int(input())
e = ''
p = 1
for i in range(n):
    for j in range(n-i-1):
        print("-",end=e)
    arr = []
    for j in range(i+1):
        arr.append(str(p))
        p+=1 
    if i%2: arr=arr[::-1]
    print('-'.join(arr))