# Insert between Characters
# The program must accept a string S (which does not contain any space) and another character CH. The program must insert the character CH between every adjacent pairs of characters in the string S.

# Boundary Condition(s):
# 1 <= Length of S <= 100

# Input Format:
# The first line contains S.
# The second line contains CH.

# Output Format:
# The first line contains a string value.

# Example Input/Output 1:
# Input:
# abcde
# :

# Output:
# a:b:c:d:e

# Explanation:
# Here the given string is abcde and the character CH is ':'.
# After inserting the character : between every adjacent pairs of characters, the string becomes a:b:c:d:e.
# So a:b:c:d:e is printed as the output.

# Example Input/Output 2:
# Input:
# k
# :

# Output:
# k

# Example Input/Output 3:
# Input:
# on
# -

# Output:
# o-n









s=input().strip()
print(input().join(list(s)))