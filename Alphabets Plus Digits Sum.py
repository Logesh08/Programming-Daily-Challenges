# Alphabets Plus Digits Sum

# The program must accept a string S which has alphabets and digits as the input. The program must find the sum of all the digits as D. Then the program must print the alphabets which are D positions from the alphabets present in the string.

# Note:
# The output must be in lowercase.

# Boundary Condition(s):
# Length of the S is from 3 to 100.

# Input Format:
# The first line contains the string S.

# Output Format:
# The first line contains the modified alphabets.

# Example Input/Output 1:
# Input:
# 435acl

# Output:
# mox

# Explanation:
# The digits are 4, 3, 5. The sum = 4 + 3 + 5 = 12.
# The alphabets are a, c, l. So a + 12 = m, c + 12 = o, l + 12 = x.

# Example Input/Output 2:
# Input:
# 1121ZU

# Output:
# ez

# Explanation:
# The digits are 1, 1, 2, 1. The sum = 1 + 1 + 2 + 1 = 5.
# The alphabets are Z, U. So z + 5 = e (circularly), u + 5 = z.








input = input().strip()
s = [c.lower() for c in input if c.isalpha()]
n = sum([int(i) for i in input if i.isdigit()])
print(''.join([ chr((ord(c)-ord('a') + n)%26 + ord('a')) for c in s]))