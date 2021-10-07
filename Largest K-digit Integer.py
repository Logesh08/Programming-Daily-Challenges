# Largest K-digit Integer
# The program must accept an integer N and a digit K as the input. The program must find the largest possible K-digit integer that can be formed using K consecutive digits in N. If there is no such integer, then the program must print -1 as the output.

# Boundary Condition(s):
# 1 <= N <= 10^9
# 1 <= K <= 9

# Input Format:
# The first line contains N.
# The second line contains K.

# Output Format:
# The first line contains an integer value representing the largest possible K-digit integer or -1.

# Example Input/Output 1:
# Input:
# 6478414
# 3

# Output:
# 841

# Explanation:
# Here N=6478414 and K=3.
# All the possible 3 digit integers are 647, 478, 784, 841 and 414.
# Here the largest possible 3-digit integer is 841. So 841 is printed as the output.

# Example Input/Output 2:
# Input:
# 600
# 4

# Output:
# -1

# Example Input/Output 3:
# Input:
# 21541094
# 4

# Output:
# 5410





a=input().strip()
b=int(input())
if(len(a)<b):
    print("-1")
else:
    maxi=0
    for i in range(len(a)):
        k=a[i:i+b]
        if(len(k)==b):
            h=int(k)
            if(h>maxi):
                maxi=h
    print(maxi)
