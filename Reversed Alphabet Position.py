# Reversed Alphabet Position
# Given a string S, for each letter in the string the program must print the reversed alphabet position letter.

# Boundary Condition(s):
# 1 <= Length of String <= 1000

# Input Format:
# The first line contains S.

# Output Format:
# The first line contains the specified output.

# Example Input/Output 1:
# Input:
# abc

# Output:
# zyx

# Example Input/Output 2:
# Input:
# Yarn

# Output:
# Bzim










alpa = ''
rev = ''
s = input().strip()
for c in range(ord('a'),ord('z')+1):
    alpa += chr(c)
    rev = chr(c) + rev 
for c in s:
    if c.islower():
        print(rev[alpa.index(c)],end='')
    else:
        print( rev[alpa.index(c.lower())].upper(),end='')