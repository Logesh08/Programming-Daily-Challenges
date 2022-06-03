# Sort Numbers - Factor Count
# The program must accept N positive integers as the input and sort them based on the factor count (lowest to highest factor count). If two numbers have the same factor count, order based on the value of the numbers in the ascending order.

# Input Format:
# The first line will contain N.
# The second line will contain N positive integers separated by a space.

# Output Format:
# The first line will contain the N positive integers (separated by a space) ordered by their factor count.

# Boundary Conditions:
# 2 <= N <= 10000

# Example Input/Output 1:
# Input:
# 5
# 18 23 100 1200 45

# Output:
# 23 18 45 100 1200

# Example Input/Output 2:
# Input:
# 3
# 29 11 101

# Output:
# 11 29 101







input()
def fact(x):
    count = 0
    for i in range(2,x+1):
        if x%i==0: count += 1
    return count
print(*sorted(list(map(int,input().split())),key = lambda x:(fact(x),x )))