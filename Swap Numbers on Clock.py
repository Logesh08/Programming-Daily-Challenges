# Swap Numbers on Clock
# The below 5*5 matrix represents a 12-hour analog clock. The asterisks in the clock represent the empty spaces.
# * 11 12 1 *
# 10 * * * 2
# 9 * * * 3
# 8 * * * 4
# * 7 6 5 *

# A boy is playing with the clock and he is swapping the numbers on the clock. The program must accept N pairs of integers as the input. Each pair represents the numbers swapped by the boy. The program must print the clock(matrix) after N swaps as the output.

# Boundary Condition(s):
# 1 <= N <= 50
# 1 <= Each integer in a pair <= 12

# Input Format:
# The first line contains N.
# The next N lines, each contains a pair of integers separated by a space.

# Output Format:
# The first five lines contain a matrix representing the clock after N swaps.

# Example Input/Output 1:
# Input:
# 3
# 12 4
# 9 7
# 8 12

# Output:
# * 11 4 1 *
# 10 * * * 2
# 7 * * * 3
# 12 * * * 8
# * 9 6 5 *

# Explanation:
# Here N=3, so the number of swaps is 3.
# After swapping 12 and 4, the matrix becomes
# * 11 4 1 *
# 10 * * * 2
# 9 * * * 3
# 8 * * * 12
# * 7 6 5 *
# After swapping 9 and 7, the matrix becomes
# * 11 4 1 *
# 10 * * * 2
# 7 * * * 3
# 8 * * * 12
# * 9 6 5 *
# After swapping 8 and 12, the matrix becomes
# * 11 4 1 *
# 10 * * * 2
# 7 * * * 3
# 12 * * * 8
# * 9 6 5 *

# Example Input/Output 2:
# Input:
# 4
# 12 6
# 3 9
# 12 3
# 6 9

# Output:
# * 11 9 1 *
# 10 * * * 2
# 12 * * * 6
# 8 * * * 4
# * 7 3 5 *





a=['*',11,12,1,'*',10,'*','*','*',2,9,'*','*','*',3,8,'*','*','*',4,'*',7,6,5,'*']
n=int(input())
for i in range(n):
    b,c=map(int,input().split())
    s,t=a.index(b),a.index(c)
    l=a[s]
    a[s]=a[t]
    a[t]=l
for i in range(5):
    for j in range(5):
        print(a[i*5+j],end=' ')
    print()