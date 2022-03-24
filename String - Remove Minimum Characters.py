# String - Remove Minimum Characters
# The program must accept a string S as the input. The program must print the minimum number of characters to be removed from the string S so that the length of the revised string must be even(possibly 0) also every two consecutive characters(non-overlapping) must be different.

# Boundary Condition(s):
# 2 <= Length of S <= 1000

# Input Format:
# The first line contains S.

# Output Format:
# The first line contains an integer value representing the minimum number of characters to be removed from S.

# Example Input/Output 1:
# Input:
# coffee

# Output:
# 2

# Explanation:
# Here S = coffee.
# The minimum number of characters to be removed from the string is 2.
# coffee -> cofe
# The length of the revised string is 4 which is even and every two consecutive characters are different.
# Hence 2 is printed as the output.

# Example Input/Output 2:
# Input:
# dddeeeeddd

# Output:
# 6

# Explanation:
# Here S = dddeeeeddd.
# The minimum number of characters to be removed from the string is 6.
# dddeeeeddd -> deed
# The length of the revised string is 4 which is even and every two consecutive characters are different.
# Hence 6 is printed as the output.

# Example Input/Output 3:
# Input:
# grapes

# Output:
# 0

# Example Input/Output 4:
# Input:
# aabbaaabbbc

# Output:
# 3






s=input().strip()
s2=""
i=0
while i<len(s)-1:
    if s[i]!=s[i+1]:
        s2+=s[i]
        s2+=s[i+1]
        i+=1
    i+=1
print(len(s)-len(s2))