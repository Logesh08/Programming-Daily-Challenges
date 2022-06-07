# Sliding Window Maximum
# Given a list of N positive integers and a sliding window of size W, the program must print the compare the maximum value CURRMAX present in the specific window instance with that of the previous window maximum PREVMAX and print the maximum value of CURRMAX and PREVMAX. The maximum values must be separated by a space.

# Input Format:
# The first line contains N and W separated by a space.
# The second line contains N integer values separated by a space.

# Output Format:
# The first line contains the maximum values separated by a space.

# Boundary Conditions:
# 1 <= N <= 10000
# W <= N

# Example Input/Output 1:
# Input:
# 7 3
# 10 3 8 4 2 11 1

# Output:
# 10 10 8 11 11








n,w = map(int,input().split())
arr = list(map(int,input().split()))
preMax = 0
window = [arr.pop(0) for _ in range(w)]
while arr:
    x = max(window)
    print(max([preMax,x]),end=' ')
    preMax = x 
    window.pop(0)
    window.append(arr.pop(0))
print(max([preMax,max(window)]))