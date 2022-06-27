# Tenth Digit Odd Average
# An array of N integers is passed as input. The program must print the average of the integers having their tenth digit as an odd digit. The average is rounded up to two decimal places.

# Boundary Condition(s):
# 1 <= N <= 9999

# Input Format:
# The first line contains N.
# The second line contains N integers separated by space(s).

# Output Format:
# The first line contains the average rounded up to two decimal places.

# Example Input/Output 1:
# Input:
# 5
# 10 2334 65 76 80

# Output:
# 806.67

# Example Input/Output 2:
# Input:
# 7
# 30 15 41 24 48 27 34

# Output:
# 26.33






input()
arr = [int(i) for i in input().split() if len(i)>1 and int(i[-2])%2]
print("%.2f"%(sum(arr)/len(arr)) if arr else "0.00")