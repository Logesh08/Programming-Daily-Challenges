# Skip Bad Tiles
# A very narrow lane has a single row of N large tiles. Due to a recent rains, some of these N tiles have broken and indicated by the letter 'B'. If a person lands on a broken tile, he will fall into a ditch which is below the tiles. A person who is standing on Kth tile in a single step can land on (K+1)th or (K+2)th tile. Find the least number of steps S in which a person can land the Nth tile starting from the 1st tile. It is given that the 1st and the Nth tile will never be broken as they have pillar support. The tiles which are not broken are indicated by the letter 'G'.

# Input Format:
# The first line contains N.
# The second lines contain N values which are either 'G' or 'B'

# Output Format:
# The first line contains S.

# Boundary Conditions:
# 1 <= N <= 50

# Example Input/Output 1:
# Input:
# 7
# G G B G G B G

# Output:
# 4

# Example Input/Output 2:
# Input:
# 4
# G B G G

# Output:
# 2











n = int(input())
arr = input().split()
count=0
while arr:
    if arr[0]=='G' and len(arr)>1 and arr[1]=='B':
        count+=1
        arr.pop(0)
        arr.pop(0)
    elif len(arr)>2 and arr[0]=='G' and arr[2]=='G':
        count+=1
        arr.pop(0)
        arr.pop(0)
        
    elif arr[0]=='G' and len(arr)>1 and arr[1]=='G':
        count+=1
        arr.pop(0)
        
    elif arr[0]=='B':
        count+=1
        arr.pop(0)
        
    else:
        break
print(count)