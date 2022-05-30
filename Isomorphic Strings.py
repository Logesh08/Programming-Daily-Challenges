# Isomorphic Strings
# Given two strings S1 and S2, the program must print if they are isomorphic or not.

# Two strings are isomorphic if the characters in S1 can be replaced to get S2 based on the conditions given below.
# - All occurrences of a character must be replaced with another character while preserving the order of characters.
# - No two characters can map to the same character but a character can map to itself.

# Input Format:
# The first line contains S1
# The second line contains S2

# Output Format:
# The first line contains YES or NO indicating if S1 and S2 are isomorphic or not.

# Boundary Conditions:
# 1 <= Length of S1 and S2 <= 1000

# Example Input/Output 1:
# Input:
# fill
# bell

# Output:
# YES

# Example Input/Output 2:
# Input:
# paper
# title

# Output:
# YES


# Example Input/Output 3:
# Input:
# pen
# egg

# Output:
# NO










a = input(). strip()  
b = input() .strip()    
t = b
for c in range( len(b)): 
    if b[c] != '*' : 
        a = a. replace(a[c] ,b[c]) 
        b = b. replace(b[c] , '*')
print('YES' if a==t  else 'NO')

## Another Method
## https://www.geeksforgeeks.org/check-if-two-given-strings-are-isomorphic-to-each-other/