# Nearest Multiple of 10

# The program must accept an integer N as the input. The program must print the nearest multiple of 10 as the output.
# Note: If the value of N has two nearest multiples, then the smaller multiple should be printed as the output.

# Boundary Condition(s):
# 10 <= N <= 999999999

# Input Format:
# The first line contains the value of N.

# Output Format:
# The first line contains the nearest multiple of 10.

# Example Input/Output 1:
# Input:
# 551

# Output:
# 550

# Example Input/Output 2:
# Input:
# 9999999

# Output:
# 10000000






s = list(input().strip())
for i in range(len(s))[::-1]:
    if s[i]!='9' and i!=0:
        if int(s[i])>5:
            s[i-1] = str(int(s[i-1])+1)
        s[i]='0'
        break
    else:
        s[i]='0'
if s[0]=='0': s=['1']+s
print(''.join(s))