# Append N Strings
# N string values are passed as input. The program must append the N strings in the reverse order and print the single string as the output.

# Input Format:
# The first line contains N.
# Next N lines contain the N string values.

# Output Format:
# The first line contains the combined string value.

# Boundary Conditions:
# 2 <= Length of a String Value <= 50

# Example Input/Output 1:
# Input:
# 3
# apple
# boy
# cat

# Output:
# catboyapple



n = int(input())
arr = [input().strip() for i in range(n)]
print(''.join(arr[::-1]))