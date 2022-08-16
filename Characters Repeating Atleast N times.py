# Characters Repeating Atleast N times

# The program must accept a string S and an integer N as input. The program must print the characters repeating consecutively at least N times as the output.

# Boundary Condition(s):
# 2 <= Length of String S <= 100
# 1 <= N <= 10

# Input Format:
# The first line contains the value of string S.
# The second line contains the value of N.

# Output Format:
# The first line contains the characters repeating consecutively at least N times.

# Example Input/Output 1:
# Input:
# aabccbhhhh
# 2

# Output:
# ach

# Example Input/Output 2:
# Input:
# aaaabbcccbb
# 3

# Output:
# ac







s = input().strip()
n = int(input())
c = s[0]
t = c
for i in s[1:]:
    if i==c:
        t += c
    else:
        if len(t)>=n:
            print(t[0],end='')
        c = i 
        t = i 
if len(t)>=n:
    print(t[0],end='')