# Same Bits - Odd Positions
# The program must accept two integers X and Y as the input. The program must print an integer C whose binary representation indicates the same bits at the odd positions from LSB(Least Significant Bit) of the integers X and Y. If there are no bits same at odd positions, then the program must print -1 as the output.

# Boundary Condition(s):
# 1 <= X, Y <= 10^8

# Input Format:
# The first line contains X and Y separated by a space.

# Output Format:
# The first line contains C.

# Example Input/Output 1:
# Input:
# 109 107

# Output:
# 5

# Explanation:
# 109 -> 1101101
# 107 -> 1101011
# 1st position from LSB: Same bit 1
# 3rd position from LSB: Different bits
# 5th position from LSB: Same bit 0
# 7th position from LSB: Same bit 1
# 101 -> 5

# Example Input/Output 2:
# Input:
# 206 27

# Output:
# -1

# Explanation:
# 206 -> 11001110
# 27 -> 00011011
# 1st position from LSB: Different bits
# 3rd position from LSB: Different bits
# 5th position from LSB: Different bits
# 7th position from LSB: Different bits
# So -1 is printed.

# Example Input/Output 3:
# Input:
# 337 347

# Output:
# 29

# Explanation:
# 337 -> 101010001
# 347 -> 101011011
# 1st position from LSB: Same bit 1
# 3rd position from LSB: Same bit 0
# 5th position from LSB: Same bit 1
# 7th position from LSB: Same bit 1
# 9th position from LSB: Same bit 1
# 11101 -> 29





a,b=map(int,input().split())
a=bin(a)[2:];b=bin(b)[2:];s=""
if len(a)<len(b):
    a='0'*(len(b)-len(a))+a
else:
    b='0'*(len(a)-len(b))+b
a=a[::-1];b=b[::-1]
for i in range(0,len(a),2):
    if a[i]==b[i]:
        s+=a[i]
if s:
    print(int(s[::-1],2))
else:
    print("-1")