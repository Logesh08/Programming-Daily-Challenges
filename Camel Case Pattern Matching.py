# Camel Case Pattern Matching
# The program must accept two string values S and P as the input. The string P represents a pattern and the string S represents a string to be matched with the pattern P. The program must print YES if the string S matches the pattern P. Else the program must print NO as the output. The string S matches the pattern P if and only if we can insert lower case alphabets in P so that it is equal to the string S.

# Boundary Condition(s):
# 1 <= Length of S, P <= 1000

# Input Format:
# The first line contains S.
# The second line contains P.

# Output Format:
# The first line contains either YES or NO.

# Example Input/Output 1:
# Input:
# FootBall
# FoBa

# Output:
# YES

# Explanation:
# Here S = FootBall and P = FoBa.
# After inserting the lower case characters o, t, l and l in the string P, the string P becomes FootBall.
# Hence the output is YES.

# Example Input/Output 2:
# Input:
# GreedyAlgorithm
# GAl

# Output:
# YES

# Example Input/Output 3:
# Input:
# MondayToTuesday
# MoTo

# Output:
# NO

# Example Input/Output 4:
# Input:
# NorthEastSouth
# NooES

# Output:
# NO
















s = input().strip()
n = input().strip()
def getArray(s):
    arr = []
    while len(s)>1 and s[0].islower():
        s=s[1:]
    t=s[0]
    for c in s[1:]:
        if c.isupper():
            arr.append(t)
            t=c
        else:
            t+=c
    arr.append(t)
    return arr
s=(getArray(s))
n=(getArray(n))
for i in range(len(s)):
    if len(n)!=len(s) or n[i] not in s[i]:
        print('NO')
        exit()
print('YES')