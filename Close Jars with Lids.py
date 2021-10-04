# Close Jars with Lids
# The program must accept N integers as the input. Each odd integer represents a jar. Each even integer represents a lid. A jar X can be closed with lid X+1.
# The program must print the number of jars that can be closed with lid as the output.

# Boundary Condition(s):
# 1 <= N <= 100
# 1 <= Each integer value <= 10^9

# Input Format:
# The first line contains N.
# The second line contains N integer values separated by a space.

# Output Format:
# The first line contains an integer value representing the number of jars that can be closed with a lid.

# Example Input/Output 1:
# Input:
# 6
# 1 2 4 3 10 11

# Output:
# 2

# Explanation:
# 1, 3 and 11 represent the jars.
# 2, 4 and 10 represent the lids.
# Jar 1 can be closed with lid 2.
# Jar 3 can be closed with lid 4.

# Example Input/Output 2:
# Input:
# 4
# 100 101 102 103

# Output:
# 1




n=int(input())
valid=0
arr = list(map(int,input().split()))
arr.sort(key= lambda x:-(x&1))
while arr and arr[0]&1:
    val=arr.pop(0)+1
    if val in arr:
        arr.remove(val)
        valid+=1
print(valid)
