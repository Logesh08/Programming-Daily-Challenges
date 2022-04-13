# Special Number
# An integer N is a special number if N can be expressed as a sum of an integer X and its reverse. The program must print if N is a special number or not.

# Boundary Condition(s):
# 1 <= N <= 10^6

# Input Format:
# The first line contains N.

# Output Format:
# The first line contains true or false.

# Example Input/Output 1:
# Input:
# 22

# Output:
# true

# Explanation:
# Here N=22.
# Consider X=11. The reverse is also 11. 
# As 11+11 = 22, N is a special number.

# Example Input/Output 2:
# Input:
# 121

# Output:
# true

# Explanation:
# When X=56, the reverse is 65.
# 56+65 = 121. Hence 121 is a special number.

# Example Input/Output 3:
# Input:
# 15

# Output:
# false








n = int(input())
for i in range(n//2 + n%2,0,-1):
    x = int(str(n-i))
    if int(str(i)) == int(str(x)[::-1]):
        print('true')
        exit()
print('false')