# Remove Trailing Zeros

# The program must accept N integers as the input. The program must remove the trailing zeros for all the N integers. Then the program must print the smallest integer among the N modified integers as the output.

# Boundary Condition(s):
# 1 <= N <= 100
# 1 <= Each integer value <= 10^8

# Input Format:
# The first line contains N.
# The second line contains N integers separated by a space.

# Output Format:
# The first line contains the smallest integer among the N modified integers.

# Example Input/Output 1:
# Input:
# 5
# 150 2000 50 8800 24

# Output:
# 2

# Explanation:
# After removing the trailing zeros in the five integers, the integers become 15 2 5 88 24.
# Now the smallest integer is 2. So 2 printed as the output.

# Example Input/Output 2:
# Input:
# 4
# 10 19 457 1000000

# Output:
# 1



# Max Execution Time Limit: 1000 millisecs






n = input()
arr = list(map(lambda x: int(x.rstrip('0')),input().split()))
print(min(arr))