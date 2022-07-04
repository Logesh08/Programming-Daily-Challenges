# Hundredth Digit Odd
# Three numbers A, B, C are passed as input. The program must print the first occurring number having an odd digit in its hundredth place. Atleast one number will have its hundredth digit as an odd digit.

# Boundary Condition(s):
# 1 <= A, B and C <= 999999999

# Input Format:
# The first line contains A, B and C separated by a space.

# Output Format:
# The first line contains an integer.

# Example Input/Output 1:
# Input:
# 12345 400 3478

# Output:
# 12345

# Example Input/Output 2:
# Input:
# 3439 849 567

# Output:
# 567










arr = input().split()
for i in arr:
    if len(i)>2 and int(i[-3])%2:
        print(i)
        exit()