# Integers - Divide and Add Remainders
# The program must accept N integers and an integer K. Starting from the 1st element to the Kth element, the program must divide the integers starting from the K+1th element and add the respective remainders to the array elements. The program must finally print the revised array values.

# Boundary Condition(s):
# 1 <= K < N <= 100
# 1 <= Each integer value <= 10^5

# Input Format:
# The first line contains N.
# The second line contains N integer values separated by a space.
# The third line contains K.

# Output Format:
# The first line contains the revised array values separated by a space.

# Example Input/Output 1:
# Input:
# 5
# 10 24 61 78 90
# 2

# Output:
# 10 24 76 100 108

# Explanation:
# Here K=2.
# After dividing by 10 and adding the remainders the array becomes
# 10 24 62 86 90.

# After dividing by 24 and adding the remainders the array becomes
# 10 24 76 100 108.

# Example Input/Output 2:
# Input:
# 6
# 12 49 86 57 18 63
# 3

# Output:
# 12 49 86 166 96 166




n=int(input())
arr=list(map(int,input().split())) 
k=int(input())
for i in range(k):
    for j in range(k,n):
        arr[j]+=arr[j]%arr[i]
print(*arr)