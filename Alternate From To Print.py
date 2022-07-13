# Alternate From To Print

# An array of N integers is given as input. The program must print the 1st to 2nd element in ascending order, print from 2nd to 3rd element in descending order, print from 3rd to 4th element in ascending order and so on.

# Boundary Condition(s):
# 3 <= N <= 100

# Input Format:
# The first line contains N.
# The second line contains N integers separated by space(s).

# Output Format:
# The first line contains the integer values separated by space(s).

# Example Input/Output 1:
# Input:
# 5
# 1 5 10 20 28

# Output:
# 1 2 3 4 5 10 9 8 7 6 5 10 11 12 13 14 15 16 17 18 19 20 28 27 26 25 24 23 22 21 20

# Example Input/Output 2:
# Input:
# 4
# 1 10 17 25

# Output:
# 1 2 3 4 5 6 7 8 9 10 17 16 15 14 13 12 11 10 17 18 19 20 21 22 23 24 25









n = int(input())
arr = list(map(int,input().split()))
for i in range(1,n):
    r = range(arr[i-1],arr[i]+1)
    if i%2==0: r=r[::-1]
    for j in r:
        print(j,end=' ')