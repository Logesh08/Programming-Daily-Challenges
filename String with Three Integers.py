# String with Three Integers
# The program must accept two nonzero digits D1, D2 and a string S as the input. The program must form three integers A, B and C based on the following conditions.
# A = D1
# B = (A*10)+D2
# C = (B*10)+D2
# The program must print Yes if the given string S is formed by the concatenation of integers A, B and C (in any order and any number of times). Else the program must print No as the output.

# Note:
# - The values of D1 and D2 are always not equal.
# - The string S always contains nonzero digits.

# Boundary Condition(s):
# 1 <= D1, D2 <= 9
# 1 <= Length of S <= 100

# Input Format:
# The first line contains D1 and D2 separated by a space.
# The second line contains S.

# Output Format:
# The first line contains Yes or No.

# Example Input/Output 1:
# Input:
# 1 3
# 11313313

# Output:
# Yes

# Explanation:
# Here D1 = 1, D2 = 3 and S = "11313313".
# A = 1, B = 13 and C = 133.
# 11313313 -> 1 13 133 13 -> Concatenation of A, B, C and B.

# Example Input/Output 2:
# Input:
# 5 2
# 25222

# Output:
# No

# Example Input/Output 3:
# Input:
# 6 9
# 696969677

# Output:
# No









a , b = map(int,input().split()) 
s = input().strip()
x = a 
y = (x*10) + b 
z = (y*10) + b
for i in [z,y,x]:
    s = ''.join(s.split(str(i))) 
print('No' if s else 'Yes')