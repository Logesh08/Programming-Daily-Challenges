# Print First and Last Character
# A string S is passed as input. The program must print the first and last character of the string.

# Boundary Condition(s):
# 1 <= length of String <= 1000

# Input Format:
# The first line contains the string S.

# Output Format:
# The first line contains two characters.

# Example Input/Output 1:
# Input:
# hello

# Output:
# ho

# Example Input/Output 2:
# Input:
# mango

# Output:
# mo







(lambda x: print(x[0]+x[-1]))(input())