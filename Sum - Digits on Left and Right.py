# Sum - Digits on Left and Right
# The program must accept an integer N containing only nonzero digits as the input. For each digit D in the integer N, the program must form an integer by concatenating D digits on the left and D digits on the right of the D. Then the program must print the sum of the resulting integer values. If the number of digits on the left or right is less than D, then consider only the existing digits on the left or right.

# Boundary Condition(s):
# 10 <= N <= 10^8

# Input Format:
# The first line contains N.

# Output Format:
# The first line contains an integer value representing the sum of resulting integer values.

# Example Input/Output 1:
# Input:
# 2314

# Output:
# 510

# Explanation:
# Here N = 2314.
# 2 -> 31
# 3 -> 214
# 1 -> 34
# 4 -> 231
# 31 + 214 + 34 + 231 = 510.

# Example Input/Output 2:
# Input:
# 541326

# Output:
# 201089

# Explanation:
# 5 -> 41326
# 4 -> 51326
# 1 -> 43
# 3 -> 54126
# 2 -> 136
# 6 -> 54132
# 41326 + 51326 + 43 + 54126 + 136 + 54132 = 201089.










s = input().strip()
Sum = 0
for i in range(len(s)):
    c = int(s[i])
    t = ''
    for j in range(i-c,i):
        if j>=0:
            t+=(s[j])
    for j in range(i+1,i+c+1):
        if j>=len(s): break
        t+=(s[j])
    Sum+=int(t)
print(Sum)