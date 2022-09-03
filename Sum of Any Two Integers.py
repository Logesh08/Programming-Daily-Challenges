# Sum of Any Two Integers

# The program must accept an integer value M and a list of N integers as input. The program must print all the combinations of two integers x and y where x+y = M. x <= y and the smallest possible value of x must come first in the output. x values must be printed in the order of the occurence.

# Boundary Condition(s):
# 1 <= M <= 200
# 4 <= Size of the list (N) <= 100000

# Input Format:
# The first line contains the value of M.
# The second line contains the list of integers separated by space(s).

# Output Format:
# The list of lines contain all the combinations of two integers giving the sum equal to M.

# Example Input/Output 1:
# Input:
# 10
# 2 4 6 8 5

# Output:
# 2 8
# 4 6

# Explanation:
# In the above list of numbers, 2 + 8 = 10 and 4 + 6 = 10.
# Hence the combinations 2 8 and 4 6 are printed.

# Example Input/Output 2:
# Input:
# 50
# 25 20 25 30 15 45 45 5

# Output:
# 5 45
# 20 30
# 25 25





m = int(input())
arr = list(map(int,input().split()))
n = len(arr)
ans = []
for i in range(n):
    for j in range(i+1,n):
        x,y = arr[i],arr[j]
        if arr[i]+arr[j]==m and sorted([x,y]) not in ans:
            ans.append(sorted([x,y]))
for i in sorted((ans)):
    print(*i)