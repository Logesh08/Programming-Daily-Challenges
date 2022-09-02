# Integer with Largest Digits Sum

# The program must accept an integer N as the input. The program must print an integer from 1 to N which has the largest sum of digits as the output. If more than one integers contain the largest digits sum, then the program must print the largest integer among them as the output.

# Boundary Condition(s):
# 1 <= N <= 1000

# Input Format:
# The first line contains the value of N.

# Output Format:
# The first line contains the integer with the largest digits sum.

# Example Input/Output 1:
# Input:
# 100

# Output:
# 99

# Explanation:
# sum of digits in 1 is 1
# sum of digits in 2 is 2
# .
# .
# sum of digits in 98 is 17
# sum of digits in 99 is 18
# sum of digits in 100 is 1
# From 1 to 100, 99 has the largest digit sum (9 + 9 = 18).

# Example Input/Output 2:
# Input:
# 48

# Output:
# 48

# Example Input/Output 3:
# Input:
# 521

# Output:
# 499





x = int(input())
n = list(str(x).strip())
n[0] = int(n[0])-1 
mb = int(str(n[0])+('9'*len(n[1:])))
print(mb if sum(list(map(int,str(mb)))) > sum(list(map(int,str(x)))) else x)