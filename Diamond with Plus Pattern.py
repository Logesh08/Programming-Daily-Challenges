# Diamond with Plus Pattern
# The program must accept an integer N as the input. The program must print (2*N)-1 lines of pattern as shown in the Example Input/Output section. The asterisks in the pattern indicate the diamond and plus symbols. The hyphens in the pattern indicate the empty spaces.

# Boundary Condition(s):
# 2 <= N <= 50

# Input Format:
# The first line contains N.

# Output Format:
# The first (2*N)-1 lines contain the desired pattern as shown in the Example Input/Output section.

# Example Input/Output 1:
# Input:
# 5

# Output:
# --------*
# ------*-*-*
# ----*---*---*
# --*-----*-----*
# *-*-*-*-*-*-*-*-*
# --*-----*-----*
# ----*---*---*
# ------*-*-*
# --------*

# Explanation:
# Here N=5, so the pattern contains 9 lines ((2*5)-1) of output.

# Example Input/Output 2:
# Input:
# 3

# Output:
# ----*
# --*-*-*
# *-*-*-*-*
# --*-*-*
# ----*

# Example Input/Output 3:
# Input:
# 6

# Output:
# ----------*
# --------*-*-*
# ------*---*---*
# ----*-----*-----*
# --*-------*-------*
# *-*-*-*-*-*-*-*-*-*-*
# --*-------*-------*
# ----*-----*-----*
# ------*---*---*
# --------*-*-*
# ----------*



n=int(input())
print("-"*(2*(n-1)),end="*\n")

for i in range(1,n-1):
    for j in range((n+1)-(i*2) + 2):
        print("-",end='')
    print(end="*")
    for j in range((i*2) -1 ):
        print(end='-')
    print(end="*")
    for j in range((i*2) -1 ):
        print(end='-')
    print(end="*\n")
print("*-"*(n-1)*2,end='*\n')
for i in range(n-1, 1 ,-1):
    for j in range((n+1)-(i*2) + 4):
        print(end='-')
    print(end='*')
    for j in range(((i-1)*2) -1 ):
        print(end='-')
    print(end='*')
    for j in range(((i-1)*2) -1 ):
        print(end='-')
    print("*")
print("-"*(2*(n-1)),end="*")