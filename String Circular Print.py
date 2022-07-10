# String Circular Print
# A string S and an integer N is passed as input. The program must traverse and print N alphabet letters in the string circularly.
# Note: All the alphabets in the string S is only in lowercase.

# Boundary Condition(s):
# 2 <= Length of String <= 1000

# Input Format:
# The first line contains the string S.
# The second line contains N.

# Output Format:
# The first line contains the N alphabet letters.

# Example Input/Output 1:
# Input:
# hello
# 7

# Output:
# hellohe

# Example Input/Output 2:
# Input:
# yum
# 7

# Output:
# yumyumy








s = input().strip()
for i in range(int(input())):
    print(s[i%len(s)],end='')
    
    
    
    
# One Liner    
(lambda x,y: print(*[x[i%len(x)] for i in range(y)],sep=''))(input(),int(input()))