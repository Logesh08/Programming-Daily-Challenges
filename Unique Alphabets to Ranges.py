# Unique Alphabets to Ranges
# The program must accept a string S containing only lower case alphabets as the input. The program must find the unique alphabets in the given string and print the alphabets as ranges in sorted order as shown in the Example Input/Output section.

# Boundary Condition(s):
# 1 <= Length of S <= 100

# Input Format:
# The first line contains S.

# Output Format:
# The lines contain the alphabets ranges in sorted order.

# Example Input/Output 1:
# Input:
# fhjgipqrtsifif

# Output:
# f:j
# p:t

# Explanation:
# Here S = fhjgipqrtsifif.
# The unique alphabets present in the string S are given below.
# f g h i j p q r s t
# 1st range -> f:j
# 2nd range -> p:t

# Example Input/Output 2:
# Input:
# abbackxxyzzponm

# Output:
# a:c
# k:k
# m:p
# x:z





s = sorted(list(set(input().strip())))
start = s.pop(0)
ans = []
while s:
    x = s.pop(0)
    if ord(start[-1])+1 == ord(x):
        start+=x 
    else:
        ans.append(start)
        start = x
ans.append(start)
for ans in ans:print(ans[0]+':'+ans[-1])