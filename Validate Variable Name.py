# Validate Variable Name
# The program must accept a string S representing a variable name as the input. The program must validate the given variable name based on the following conditions.
# - Only English letters, digits and underscore are allowed.
# - The variable name must not start with digits.
# The program must print YES if the given variable name is valid. Else the program must print NO as the output.

# Boundary Condition(s):
# 1 <= Length of S <= 50

# Input Format:
# The first line contains S.

# Output Format:
# The first line contains YES or NO.

# Example Input/Output 1:
# Input:
# Max_1_count

# Output:
# YES

# Explanation:
# The given variable name starts with an English letter and does not contain any characters other than English letters, digits and underscore.
# Hence it is a valid variable name.
# So YES is printed as the output.

# Example Input/Output 2:
# Input:
# 2_min

# Output:
# NO

# Example Input/Output 3:
# Input:
# onesCount#1

# Output:
# NO

# Example Input/Output 4:
# Input:
# max Value

# Output:
# NO








s = input().strip()
if s[0].isdigit():
    print('NO')
    exit()
for i in s:
    if not(i.isalpha() or i.isdigit() or i=='_'):
        print('NO')
        exit()
print('YES')