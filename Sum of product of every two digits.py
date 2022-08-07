# Sum of product of every two digits

# The program must accept an integer N as the input. The program must print the sum of the product of every two digits in the integer N.
# Note: If a two digit number is not formed in the last part of the integer N, then consider only the last digit.

# Boundary Condition(s):
# 1 <= N <= 10^17

# Input Format:
# The first line contains the value of N.

# Output Format:
# The first line contains the sum of the product of every two digits in the integer N.

# Example Input/Output 1:
# Input:
# 1234567

# Output:
# 800

# Explanation:
# 12*34 + 56*7 -> 408+392 -> 800

# Example Input/Output 2:
# Input:
# 120014

# Output:
# 14

# Explanation:
# 12*0 + 14 -> 0+14 -> 14







n = input().strip()
arr = []
for i in range(0,len(n),2):
    arr.append(n[i:i+2])
ans = []
for i in range(0,len(arr),2):
    ans.append(int(arr[i])*int(arr[i+1]) if i+1 < len(arr) else int(arr[i]))
print(sum(ans))