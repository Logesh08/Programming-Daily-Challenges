# Inverted V Pattern

# The program must accept the values of string S1 and S2 as input. The program must print the desired pattern as shown in the Example Input/Output section.

# Boundary Condition(s):
# 2 <= Length of S1, S2 <= 100

# Input Format:
# The first line contains the value of string S1.
# The second line contains the value of string S2.

# Output Format:
# The list of lines contain the desired pattern as shown in the Example Input/Output section.

# Example Input/Output 1:
# Input:
# orange
# energy 

# Output:
# -----e
# ----g-n
# ---n---e
# --a-----r
# -r-------g
# o---------y

# Example Input/Output 2:
# Input:
# apple
# orange

# Output:
# -1

# Example Input/Output 3:
# Input:
# neuro 
# lemon

# Output:
# ----n
# ---o-e
# --m---u
# -e-----r
# l-------o





a = input().strip()
b = input().strip()
if a[0]==b[-1] or b[0]==a[-1]:
    if a[0]==b[-1]: a,b=b,a
    print('-'*(len(a)-1)+b[0])
    for i in range(1,len(a)):
        print(('-'*(len(a)-i-1))+a[-i-1],end='-'*((i-1)*2 +1))
        print(b[i])
        
else:
    print(-1)