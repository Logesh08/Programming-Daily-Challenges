# Digits Asterisks Pattern
# The program must accept a string S containing only digits as the input. The program must print the digits in the string S based on the following conditions.
# - The digits of the same value must be printed on the same line.
# - The values of the digits must be printed in the order of their occurrence.
# - The empty spaces in each row must be printed as asterisks.

# Boundary Condition(s):
# 1 <= Length of S <= 100

# Input Format:
# The first line contains S.

# Output Format:
# The lines contain the digits and asterisks based on the given conditions.

# Example Input/Output 1:
# Input:
# 1225644789964

# Output:
# 1 * *
# 2 2 *
# 5 * *
# 6 6 *
# 4 4 4
# 7 * *
# 8 * *
# 9 9 *

# Example:
# Here S = 1225644789964.
# 1 occurs one time.
# 2 occurs two times.
# 5 occurs one time.
# 6 occurs two times.
# 4 occurs three times.
# 7 occurs one time.
# 8 occurs one time.
# 9 occurs two times.

# Example Input/Output 2:
# Input:
# 624655622653

# Output:
# 6 6 6 6
# 2 2 2 *
# 4 * * *
# 5 5 5 *
# 3 * * *

# Example Input/Output 3:
# Input:
# 1234567

# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7












s = list(input().strip())
maxx = 0
for i in range(10):
    maxx = max([maxx,s.count(str(i))])
while s:
    x = s.pop(0)
    print(x,end=' ')
    count = 1
    while x in s:
        print(x,end=' ')
        s.remove(x)
        count+=1 
    print('* '*(maxx-count))