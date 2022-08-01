# Common Integers between M and N

# Accept a list of M and N integers as the input. The program must print the common unique integers between the two lists M and N in the order given in M. If there is no common unique integer then the program must print "Invalid" as the output.

# Boundary Condition(s):
# 1 <= M <= 50
# 0 <= N <= M
# 0 <= Values of integers <= 999

# Input Format:
# The first line contains the value of M and N separated by space(s).
# The second line contains M integers separated by space(s).
# The third line contains N integers separated by space(s).

# Output Format:
# The first line contains the common unique integers separated by space or "Invalid".

# Example Input/ Output 1:
# Input:
# 7 3
# 3 5 7 1 6 2 8
# 1 2 7

# Output:
# 7 1 2

# Example Input/ Output 2:
# Input:
# 4 4
# 3 4 1 0
# 0 1 1 9

# Output:
# 1 0









m,n = map(int,input().split())
if n==0:
    print('Invalid')
    exit()
a = list(map(int,input().split()))
b = list(map(int,input().split()))
arr = []
for i in a:
    if i in b and i not in arr:
        arr.append(i)
print(*arr if arr else ['Invalid'])