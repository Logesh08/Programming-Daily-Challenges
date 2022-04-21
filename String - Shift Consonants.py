# String - Shift Consonants
# The program must accept a string S containing only alphabets as the input. The program must shift the consonants to the left by 1 position in the string S. Then the program must print the revised string as the output.

# Note: At least one consonant is always present in the string S.

# Boundary Condition(s):
# 1 <= Length of S <= 1000

# Input Format:
# The first line contains S.

# Output Format:
# The first line contains the revised string S.

# Example Input/Output 1:
# Input:
# Gujarat

# Output:
# jurataG

# Explanation:
# Here S = Gujarat.
# The consonants in the string S are G, j, r, and t.
# After shifting the consonants to the left by 1 position, the string S becomes jurataG.
# So jurataG is printed as the output.

# Example Input/Output 2:
# Input:
# TooL

# Output:
# LooT









s = list(input().strip())
v = 'aeiouAEIOU'
arr = []
for i in range(len(s)):
    c = s[i]
    if c not in v:
        s[i] = '*'
        arr.append(c)
s = s[::-1]
s[s.index('*')] = arr.pop(0)
s = s[::-1]
for i in range(len(s)):
    if s[i] == '*':
        s[i] = arr.pop(0)
print(''.join(s))