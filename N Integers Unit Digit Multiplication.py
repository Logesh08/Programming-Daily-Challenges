# N Integers Unit Digit Multiplication

# The program must accept N integers as input. The program must print the N integers multiplied by the unit digit of previous integer. The first integer has no previous integer, so it is multiplied by the unit digit of Nth integer.

# Boundary Condition(s):
# 2 <= N <= 100

# Input Format:
# The first line contains the N.
# The second line contains the N integers separated by space(s).

# Output Format:
# The first line contains the N integers.

# Example Input/Output 1:
# Input:
# 5
# 12 34 11 15 16

# Output:
# 72 68 44 15 80

# Example Input/Output 2:
# Input:
# 3
# 123 145 16

# Output:
# 738 435 80







(lambda n,arr:(print(*[int(arr[i])*int(arr[i-1][-1]) for i in range(n)])))(int(input()),input().split())