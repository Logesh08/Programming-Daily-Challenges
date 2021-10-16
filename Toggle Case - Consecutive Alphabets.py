# Toggle Case - Consecutive Alphabets
# The program must accept a string S as the input. The program must toggle the case of the alphabets if two or more alphabets of the same case occur consecutively in the string S. Then the program must print the revised string as the output.

# Boundary Condition(s):
# 2 <= Length of S <= 1000

# Input Format:
# The first line contains S.

# Output Format:
# The first line contains the revised string.

# Example Input/Output 1:
# Input:
# breadANDjam

# Output:
# BREADandJAM

# Explanation:
# Here S = breadANDjam.
# bread -> BREAD
# AND -> and
# jam -> JAM
# Now the string becomes BREADandJAM.

# Example Input/Output 2:
# Input:
# SkillRack

# Output:
# SKILLRACK

# Example Input/Output 3:
# Input:
# aAbBcCdDee

# Output:
# aAbBcCdDEE




def diff_case(x, y):
    return (x.isupper() and y.islower()) or (x.islower() and y.isupper())
s = input().strip()
master = []; ss = ''; curr_len = 0
for i in range(len(s)):
    if i != len(s)-1 and diff_case(s[i], s[i+1]):
        ss += s[i]
        master.append(ss)
        ss = ''
    else:
        ss += s[i]
        if (i == len(s)-1):master.append(ss)
        continue
print(*[i.swapcase() if len(i) >= 2 else i for i in master], sep = '')