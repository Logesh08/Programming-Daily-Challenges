# Alternate Characters Matching
# The program must accept two string values S1 and S2 having an equal even length as the input. The program must print "YES" if the alternate characters of S1 match the alternate characters of S2 ignoring the case. Else the program must print "NO" as the output.

# Boundary Condition(s):
# 2 <= Length of S1, S2 <= 100

# Input Format:
# The first line contains S1.
# The second line contains S2.

# Output Format:
# The first line contains YES or NO.

# Example Input/Output 1:
# Input:
# abcdef
# parcte

# Output:
# YES

# Explanation:
# The characters at the odd positions in S1 = "ace".
# The characters at the even positions in S2 = "ace".
# Hence YES is printed as the output.

# Example Input/Output 2:
# Input:
# abcdef
# BQDSFU

# Output:
# YES

# Example Input/Output 3:
# Input:
# abcd
# abcd

# Output:
# NO




s1=input().strip()
s2=input().strip()
flagS=True
flagF=True
for i in range(0,len(s1),2):
    if s1[i].lower()!=s2[i+1].lower():
        flagF=False
    if s2[i].lower()!=s1[i+1].lower():
        flagS=False
if(flagS or flagF):
    print('YES')
else:
    print('NO')
    