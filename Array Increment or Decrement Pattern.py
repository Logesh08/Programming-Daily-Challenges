# Array Increment or Decrement Pattern
# The program must accept an array of N integers and an integer T as the input. The program must modify the array T times based on the following conditions.
# - The program must reduce the value of an integer by 1 at a time (left to right circularly).
# - If an integer value reaches 0, then the program must start increasing the value by 1 till the integer reaches its original value. Then the program must decrement the value to 0, then increment the value to its original value, and so on.
# - After each modification, the program must print the integers in the revised array.

# Boundary Condition(s):
# 2 <= N <= 25
# 1 <= Each integer value <= 50
# 1 <= T <= 10^4

# Input Format:
# The first line contains N.
# The second line contains N integers separated by a space.
# The third line contains T.

# Output Format:
# The first T lines, each contains N integers separated by a space representing the revised array.

# Example Input/Output 1:
# Input:
# 4
# 4 2 5 1
# 25

# Output:
# 3 2 5 1
# 3 1 5 1
# 3 1 4 1
# 3 1 4 0
# 2 1 4 0
# 2 0 4 0
# 2 0 3 0
# 2 0 3 1
# 1 0 3 1
# 1 1 3 1
# 1 1 2 1
# 1 1 2 0
# 0 1 2 0
# 0 2 2 0
# 0 2 1 0
# 0 2 1 1
# 1 2 1 1
# 1 1 1 1
# 1 1 0 1
# 1 1 0 0
# 2 1 0 0
# 2 0 0 0
# 2 0 1 0
# 2 0 1 1
# 3 0 1 1

# Example Input/Output 2:
# Input:
# 5
# 4 3 2 1 4
# 30

# Output:
# 3 3 2 1 4
# 3 2 2 1 4
# 3 2 1 1 4
# 3 2 1 0 4
# 3 2 1 0 3
# 2 2 1 0 3
# 2 1 1 0 3
# 2 1 0 0 3
# 2 1 0 1 3
# 2 1 0 1 2
# 1 1 0 1 2
# 1 0 0 1 2
# 1 0 1 1 2
# 1 0 1 0 2
# 1 0 1 0 1
# 0 0 1 0 1
# 0 1 1 0 1
# 0 1 2 0 1
# 0 1 2 1 1
# 0 1 2 1 0
# 1 1 2 1 0
# 1 2 2 1 0
# 1 2 1 1 0
# 1 2 1 0 0
# 1 2 1 0 1
# 2 2 1 0 1
# 2 3 1 0 1
# 2 3 0 0 1
# 2 3 0 1 1
# 2 3 0 1 2









input()
def prov(x):
    x=int(x)
    if x>0:y=-1
    else:y=1
    return [x,x,y]
arr=list(map(prov,input().split()))
t=int(input())
for i in range(t):
    t=len(arr)
    if arr[i%t][0]==0:
        arr[i%t][0]+=1
        arr[i%t][2]=1
    else:
        m=i%len(arr)
        if arr[m][2]==-1:
            arr[m][0]-=1
        else:
            arr[m][0]+=1
    for p in arr:print(p[0],end=' ')
    print()
    if arr[i%t][1]==arr[i%t][0]: 
        arr[i%t][2]=-1