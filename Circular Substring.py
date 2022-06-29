# Circular Substring
# A string S is given as input. The program must print the substring of S, given the starting and ending position of the substring. In case the end position is less than the starting position, the substring is printed in a circular fashion.

# Boundary Condition(s):
# 2 <= Length of String <= 1000

# Input Format:
# The first line contains S, start position and end position separated by space(s).

# Output Format:
# The first line contains the substring.

# Example Input/Output 1:
# Input:
# important 2 4

# Output:
# por

# Example Input/Output 2:
# Input:
# think 3 1

# Output:
# nkth





word, start, end = input().split()
start,end = map(int,[start,end])
if start > end:
    print(word[start:]+word[:end+1])
else:
    print(word[start:end+1])