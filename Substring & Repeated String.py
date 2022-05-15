# Substring & Repeated String
# The program must accept two string values S1 and S2 as the input. The program must print YES if S1 can be formed when S2 is repeated any number of times. Else the program must print NO as the output.

# Boundary Condition(s):
# 1 <= Length of S2 <= Length of S1 <= 100

# Input Format:
# The first line contains S1.
# The second line contains S2.

# Output Format:
# The first line contains either YES or NO.

# Example Input/Output 1:
# Input:
# antantan
# ant

# Output:
# YES

# Explanation:
# Here S1 = antantan and S2 = ant.
# S1 is formed when S2 is repeated 3 times (antantant).
# Hence YES is printed as the output.

# Example Input/Output 2:
# Input:
# bookbookbook
# ookb

# Output:
# YES

# Example Input/Output 3:
# Input:
# SkillRack
# llRackSkl

# Output:
# NO







s = input().strip()
a = input().strip()
x = s.replace(a,'')
for i in range(len(a)):
    i = (a[i:]+a[:i])
    if x in i:
        print('YES')
        exit()
print('NO')