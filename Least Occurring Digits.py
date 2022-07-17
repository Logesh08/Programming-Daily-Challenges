# Least Occurring Digits

# A series of N integers is passed as input. The program must print the least occurring digit(s) in series of integers in ascending order.

# Boundary Condition(s):
# 1 <= N <= 1000

# Input Format:
# The first line contains the series of integers separated by space(s).

# Output Format:
# The first line contains the least repeated digits in ascending order separated by a space.

# Example Input/Output 1:
# Input:
# 35 81 78 84 53

# Output:
# 1 4 7

# Example Input/Output 2:
# Input:
# 12 21 68 55 71 29 60 879

# Output:
# 0








s = input() .strip() 
c = s.count(s[0] ) 
ans = [int(s[0])] 
for i in set(s): 
    if i!=' ' : 
        cur = ( s.count(i))
        if cur<c :
            c = cur
            ans = []
        if cur == c :
            ans.append( int(i) ) 
print(*sorted( ans) ) 
 