# Remove Repeated Vowels

# The program must accept a string S containing only lower case alphabets as the input. The program must remove the repeated vowels in the string S. Then the program must print the modified string S as the output.

# Boundary Condition(s):
# 1 <= Length of S <= 10^4

# Input Format:
# The first line contains S.

# Output Format:
# The first line contains the modified string S.

# Example Input/Output 1:
# Input:
# conditioner

# Output:
# cndtner

# Explanation:
# The vowels o and i are repeated in the string "conditioner". So they are removed from the string "conditioner".
# Hence the output is cndtner

# Example Input/Output 2:
# Input:
# skillrack

# Output:
# skillrack



# Max Execution Time Limit: 1000 millisecs




s = input().strip()
print(''.join(list(filter(lambda x: not (x in "aeiou" and s.count(x)>1) ,list(s) ))))