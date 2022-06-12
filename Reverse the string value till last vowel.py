# Reverse the string value till last vowel
# Given a string S, the program must reverse the string till last vowel. (All alphabets will be in smaller case and there will be no space within the string S).

# Input Format:
# The first line contains S.

# Output Format:
# The first line contains the string value reversed till last vowel

# Boundary Conditions:
# 2 <= Length of S <= 100

# Example Input/Output 1:
# Input:
# manager

# Output:
# eganamr

# Explanation:
# The last vowel is e. Hence manage is reversed and r is retained as such.







s = input().strip()
vi = 0
for i in range(len(s)):
    if s[i] in 'aeiou':
        vi=i 
print(s[:vi+1][::-1]+s[vi+1:])