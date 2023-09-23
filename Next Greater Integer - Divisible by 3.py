# Next Greater Integer - Divisible by 3

# The program must accept a positive integer N as the input. The program must print the next greater integer which is divisible by 3 and the sum of digits in it is also divisible by 3 as the output.

# Boundary Condition(s):
# 1 <= N <= 1000

# Input Format:
# The first line contains N.

# Output Format:
# The first line contains the next greater integer based on the given conditions.

# Example Input/Output 1:
# Input:
# 22

# Output:
# 24

# Explanation:
# The next greater integer which is divisible by 3 and the sum of digits in it 6 (2+4) is also divisible by 3 is 24.
# Hence 24 is the output

# Example Input/Output 2:
# Input:
# 84

# Output:
# 87





n = int(input())
while True:
    n+=1
    if n%3==0 and sum(int(c) for c in str(n))%3==0:
        print(n)
        break