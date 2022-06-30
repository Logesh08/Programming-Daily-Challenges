# Check Step Sequence
# An array of N integers is passed as input. The program must print yes if the array is a step sequence. Else the program must print no. A sequence is said to be step sequence if the adjacent elements in the sequence differ by exactly one for all the elements.

# Boundary Condition(s):
# 1 <= N <= 9999

# Input Format:
# The first line contains N.
# The second line contains N Integers separated by space(s).

# Output Format:
# The first line contains "yes" or "no".

# Example Input/Output 1:
# Input:
# 5
# 2 3 4 3 2

# Output:
# yes

# Example Input/Output 2:
# Input:
# 6
# 5 6 7 9 8 7

# Output:
# no









n = int(input())
arr = list(map(int,input().split()))
flag =True
for i in range(1,n-1):
    if abs(arr[i] - arr[i-1])!=1 or abs(arr[i] - arr[i+1])!=1:
        flag = False
print('yes' if flag else 'no')