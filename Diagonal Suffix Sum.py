# Diagonal Suffix Sum

# The program must accept an integer matrix of size NxN as input. The program must print the sum of all the suffixes of the diagonal.

# Boundary Condition(s):
# 2 <= N <= 50

# Input Format:
# The first line contains the value of N.
# The next N lines contain N integers each separated by space(s).

# Output Format:
# The first two lines contain N integers each separated by a space.

# Example Input/Output 1:
# Input:
# 3
# 5 1 6 
# 4 2 9 
# 8 7 3 

# Output:
# 16 10 8
# 10 5 3

# Explanation:
# The main diagonal sum -> 5+2+3 -> 10
# The first suffix sum of the main diagonal -> 2+3 -> 5
# The second suffix sum of the main diagonal -> 3
# Total -> 10+5+3 -> 18
# The opposite diagonal sum -> 6+2+8 -> 16
# The first suffix sum of the opposite diagonal-> 2+8 -> 10
# The second suffix sum of the opposite diagonal -> 8
# Total -> 16+10+8 ->34
# Since 34 > 18 the opposite diagonal sum and their suffixes sum are printed in the first line and the main diagonal sum and their suffixes sum are printed in the second line
 
# Example Input/Output 2:
# Input:
# 4
# 54 86 35 71 
# 78 32 85 62 
# 69 84 66 45 
# 37 79 73 30

# Output:
# 277 206 121 37
# 182 128 96 30








n = int(input())
mat = [list(map(int,input().split())) for _ in range(n)]
r = l = 0
a , b = [],[]
for i in range(n):
    t1 = t2 = 0
    for j in range(i,n):
        r += mat[j][j]
        l += mat[j][-j-1]
        t1 += mat[j][j]
        t2 += mat[j][-j-1]
    a.append(t1)
    b.append(t2)
if r>l:
    print(*a)
    print(*b)
else:
    print(*b)
    print(*a)
    