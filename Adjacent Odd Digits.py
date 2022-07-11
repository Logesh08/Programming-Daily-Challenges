# Adjacent Odd Digits
# An integer N is given as input. The program must print the digits surrounded by odd digits on both sides. (The first and last digits have only one digit adjacent to them. So consider only that single adjacent digit for them).

# Boundary Condition(s):
# 1 <= N <= 999999999999999

# Input Format:
# The first line contains the value N.

# Output Format:
# The first line contains the digits having odd adjacent digits.

# Example Input/Output 1:
# Input:
# 2353176

# Output:
# 25316

# Example Input/Output 2:
# Input:
# 386369725

# Output:
# 62







s = input()
for i in range(len(s)):
    if (i>0 and int(s[i-1])%2 and i+1<len(s) and int(s[i+1])%2) or (i==0 and int(s[i+1])%2) or (i ==len(s)-1 and int(s[i-1])%2):
        print(s[i],end='')