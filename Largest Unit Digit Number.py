# Largest Unit Digit Number
# Two integers X and Y are given as input. The program must print the integer with largest unit digit. If the unit digits are equal, then print the larger integer.

# Boundary Condition(s):
# 1 <= X, Y <= 1000000

# Input Format:
# The first line contains X and Y separated by a space.

# Output Format:
# The first line contains an integer value.

# Example Input/Output 1:
# Input:
# 51 23

# Output:
# 23

# Example Input/Output 2:
# Input:
# 77 87

# Output:
# 87








x, y  = input().split()
print(x if int(x[-1])>int(y[-1]) else y if int(y[-1])>int(x[-1]) else x if int(x)>int(y) else y)