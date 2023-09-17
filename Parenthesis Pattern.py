# Parenthesis Pattern

# The program must accept a string S as the input. The program must print the desired pattern as shown in the Example Input/Output section.

# Boundary Condition(s):
# 1 <= Length of S <= 1000

# Input Format:
# The first line contains S.

# Output Format:
# The lines containing the desired pattern as shown in the Example Input/Output section.

# Example Input/Output 1:
# Input:
# SkillRack

# Output:
# (S)killRac(k)
# S(k)illRa(c)k
# Sk(i)llR(a)ck
# Ski(l)l(R)ack
# Skil(l)Rack

# Example Input/Output 2:
# Input:
# hide

# Output:
# (h)id(e)
# h(i)(d)e



# Max Execution Time Limit: 1000 millisecs






s = input().strip()
for i in range(len(s)//2):
    arr = list(s)
    arr[i] = "(" + arr[i] + ")"
    arr[len(s) - i -1] = "(" + arr[len(s) -i - 1] + ")"
    print(''.join(arr))
    
if len(s)%2:
    s = list(s)
    s[len(s)//2] = '(' + s[len(s)//2] + ')'
    print(''.join(s))