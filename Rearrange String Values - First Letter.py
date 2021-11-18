# Rearrange String Values - First Letter
# There are N string values that start with the same letter, but some string values are reversed. The program must accept those N string values and print the N string values that indicate the original string values as the output.

# Note:
# - There will be no string that starts and ends with the same letter.
# - All string values do not end with the same letter.
# - All string values contain only lower case alphabets.

# Boundary Condition(s):
# 2 <= N <= 50
# 2 <= Length of each string <= 100

# Input Format:
# The first line contains N.
# The next N lines, each contains a string value.

# Output Format:
# The first N lines, each contains a string value.

# Example Input/Output 1:
# Input:
# 5
# rabbit
# rose
# tekcor
# egnar
# robbery

# Output:
# rabbit
# rose
# rocket
# range
# robbery

# Explanation:
# The first letter of all the 5 strings values is r.
# So the 3rd and 4th string values are reversed.
# tekcor -> rocket
# egnar -> range

# Example Input/Output 2:
# Input:
# 4
# olleh
# oah
# hacked
# dah

# Output:
# hello
# hao
# hacked
# had





n=range(int(input()))
arr=[]
for i in n:
    arr.append(input().strip())
a,b=arr[0][0],arr[0][-1]
for l in arr:
    if a not in l:
        supreme=b 
        break
    if b not in l:
        supreme=a
try:
    for l in arr:
        print(l if l[0]==supreme else l[::-1])
except:
    [print(i) for i in arr]