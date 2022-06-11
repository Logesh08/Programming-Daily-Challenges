# Print String as Matrix
# A string S is passed as the input and the input string must be printed as a matrix of C columns where each column contains an alphabet.

# Input Format:
# The first line contains S.
# The second line contains C.

# Output Format:
# The matrix with C columns containing the string value.

# Boundary Conditions:
# 2 <= Length of a String Value <= 500
# 2 <= C <= 10

# Example Input/Output 1:
# Input:
# abcdefghijklmnop
# 5

# Output:
# abcde
# fghij
# klmno
# p









s = input().strip()
n = int(input())
c = 0
for i in range(len(s)):
    if i%n==0 and i: print()
    print(s[i],end='')