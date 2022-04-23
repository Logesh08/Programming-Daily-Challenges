# Common Odd Digits - Same Position
# The program must accept two integers X and Y as the input. The program must print the integer formed by the common odd digits in the same positions starting from the unit digit of X and Y as the output.

# Note: There will be at least one common odd digit in X and Y at the same position.

# Boundary Condition(s):
# 1 <= X, Y <= 10^8

# Input Format:
# The first line contains X.
# The second line contains Y.

# Output Format:
# The first line contains an integer value based on the given conditions.

# Example Input/Output 1:
# Input:
# 1234599
# 31579

# Output:
# 359

# Explanation:
# Here the common odd digits starting from the unit digit position are 9, 5 and 3.
# So the integer is 359 which is printed as the output.

# Example Input/Output 2:
# Input:
# 12345
# 12435

# Output:
# 15











a=input().strip()[::-1]
b=input().strip()[::-1]
ans=''
for i in range(min([len(a),len(b)])):
    if int(a[i])%2 and a[i] == b[i]:
        ans = a[i]+ans
print(ans)