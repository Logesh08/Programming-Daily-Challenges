# Reverse Odd Position in String
# Given a string S, the program must reverse the characters present in odd positions of the string S.

# Boundary Condition(s):
# 1 <= Length of S <= 100

# Input Format:
# The first line contains S.

# Output Format:
# The first line contains the string value with the characters in the odd positions of S reversed

# Example Input/Output 1:
# Input:
# barcode

# Output:
# eaocrdb

# Example Input/Output 2:
# Input:
# Mediterranean

# Output:
# neeiaerrtndaM












s = input().strip()
r = s[::-1]
if len(s)%2==0:
    r = r[1:]
for i in range(len(s)):
    if i%2==0:
        print(r[i],end='')
    else:
        print(s[i],end='')
