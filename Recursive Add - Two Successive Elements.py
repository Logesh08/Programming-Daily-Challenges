# Recursive Add - Two Successive Elements
# Given N integers as input, add successive pair of elements and repeat the process until a single digit sum value is obtained.
   
# Input format :
# The first line contains the value of N.
# The second line contains the N integer values separated by a space.

# Output format:
# The first line contains the single digit sum value.

# Boundary condition :
# 2 <= N <= 20

# Example Input/Output 1:
# Input:
# 5
# 1 2 3 4 5

# Output:
# 3

# Explanation : 
# 1 2 3 4 5
#  3 5 7 9
#   8 12 16
#   20 28
#      48
     
# 1+2=3,2+3=5,3+4=7,4+5=9 
# Then 3+5=8,5+7=12,7+9=16
# Then 8+12=20,12+16=28 
# Then 20+28=48, 4+8=12 
# Finally, 1+2=3.

# Example Input/Output 2:
# Input:
# 4 
# 1 6 2 9

# Output:
# 7
# Explanation :
# 1 6 2 9
#  7 8 11
#   15 19
#   34
   
# 1+6=7,6+2=8,2+9=11 
# Then 7+8=15, 8+11=19 
# Then 15+19=34 
# Finally, 3+4 = 7
 






input()
def allAccept(x):
    if len(x)>1:
        for i in range(1,len(x)):
            x[i-1]+=x[i]
        x.pop()
        return allAccept(x)
    else:
        x = str(x[0])
        while len(x)>1:
            x = str(sum(list(map(int,list(x)))))
        return x
        
arr = list(map(int,input().split()))
print(allAccept(arr))
