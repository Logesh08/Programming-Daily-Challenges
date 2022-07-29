# String Triangle Pattern

# Accept an integer N and a string S as input. The program must print the last N characters of each word of S in the desired pattern as shown in the Example Input/Output section.
# Note: 
# Each word in S contains more than N characters.
# If there is no word to fill the pattern then use *.

# Boundary Condition(s):
# 2 <= N <= 10
# Length of the string S is between 1 and 1000.

# Input Format:
# The first line contains the integer N.
# The second line contains the string S.

# Output Format:
# The list of lines contain the last N characters in the desired pattern.

# Example Input/Output 1:
# Input:
# 3
# apple mango orange

# Output:
# ple 
# ngo nge 

# Example Input/Output 2:
# Input:
# 2
# ask happy word letter king

# Output:
# sk 
# py rd 
# er ng **   

# Explanation:
# The last 2 characters of the first word in S is "sk".
# The first line of the output must contain one word. So, "sk" is printed.
# The last 2 characters of the second and third word are "py" and "rd". 
# The second line of the output must contain two words separated by space(s). So, "py" and "rd" printed.
# The last 2 characters of the fourth and fifth word are "er" and "ng".
# The third line of the output must contain three words separated by space(s). But here, there are two words only. So, "er" and "ng" is printed. Then, for the third word "**" is printed.









n = int(input())
words = input().split()
i = 1
while words:
    for j in range(i):
        print(words.pop(0)[-n:] if words else "*"*n,end=' ')
    print()
    i += 1