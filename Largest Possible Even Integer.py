# Largest Possible Even Integer

# The program must accept an integer N as the input. The program must print the largest possible integer containing all the even digits of N as the output. If it is not possible to form such integer then the program must print -1 as the output.

# Boundary Condition(s):
# 1 <= N <= 10^8

# Input Format:
# The first line contains N.

# Output Format:
# The first line contains the largest possible integer containing all the even digits of N or -1.

# Example Input/Output 1:
# Input:
# 748009

# Output:
# 8400

# Explanation:
# The even digits in 748009 are 4 8 0 and 0. So the largest possible integer from those even digits is 8400.
# Hence the output is 8400

# Example Input/Output 2:
# Input:
# 12846

# Output:
# 8642

# Example Input/Output 3:
# Input:
# 5719

# Output:
# -1





s = input().strip()
s = list(filter(lambda x: not int(x)%2 ,sorted(s)[::-1]))
print(''.join(s) if s else -1)


# OneLiner
print(''.join(filter(lambda x: not int(x) % 2, sorted(input().split())[::-1])) or -1)