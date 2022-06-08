# String - Substring Count
# A string S is passed as the input and another string E is also passed as the input. The program must print the number of times E appears in string S. The alphabets in both S and E will be in lower case.

# Input Format:
# The first line contains S.
# The second line contains E.

# Output Format:
# The first line contains the number of times the string E is present in S.

# Boundary Conditions:
# 2 <= Length of a String Value S and E <= 500

# Example Input/Output 1:
# Input:
# eyeyeyeeyeyeeye
# eye

# Output:
# 6






s = input().strip()
f = input().strip()
count = 0
l = len(f)
for i in range(len(s)-l +1):
    if (s[i:i+l] == f):
        count+=1 
print(count)