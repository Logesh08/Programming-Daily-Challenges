# Count Binary Value in Matrix

# Accept an integer matrix with size RxC and N as input, the matrix contains only 0's and 1's. The program must print the count of the binary value of N present in the matrix (row-wise and column-wise).

# Boundary Condition(s):
# 1 <= R, C <= 49
# 1 <= N <= 100

# Input Format:
# The first line contains the integer value of R and C separated by space.
# The next R lines contain C integers each separated by space.
# The R+2th line contains the integer value of N.

# Output Format:
# The first line contains the count of the binary value of N present in the matrix (row-wise and column-wise).

# Example Input/Output 1:
# Input:
# 4 5
# 1 0 1 0 1
# 0 0 0 0 0
# 1 1 1 1 1
# 1 0 1 0 0
# 5

# Output:
# 6

# Explanation:
# The value of N = 5 and the binary representation of N is 1 0 1.
# To find row-wise,
# In 1st row, the binary value (1 0 1) occurred two times, so that row-wise count = 2.
# In the 2nd row, there is no binary value of 5 (1 0 1).
# In the 3rd row, there is no binary value of 5 (1 0 1).
# In the 4th row, the binary value of 5 (1 0 1) occured one time. So, row-wise count = 2 + 1 = 3.

# To find column-wise,
# In 1st column, the binary value of 5 (1 0 1) occurred one time, so that column-wise count = 1.
# In the 2nd column, there is no binary value of 5 (1 0 1).
# In the 3rd column, the binary value of 5 (1 0 1) occurred one time, so column-wise count = 1 + 1 = 2.
# In the 4th column, there is no binary value of 5 (1 0 1).
# In the 5th column, the binary value of 5 (1 0 1) occurred one time, so that column-wise count = 2 + 1 = 3.

# Then print the sum of the row-wise count and column-wise count is 6.

# Example Input/Output 2: 
# Input:
# 5 5
# 1 0 0 1 0
# 0 1 0 1 1
# 0 0 1 0 0
# 1 0 0 0 0
# 0 1 0 0 0
# 4

# Output:
# 9



# OneLiner
(lambda rc: (lambda mat,n:print( sum([len([1 for i in range(rc[1]-len(n)+1) if row[i:i+len(n)]==n]) for row in mat])+sum([len([1 for i in range(rc[0]-len(n)+1) if row[i:i+len(n)]==n]) for row in map(list,zip(*mat))])))([input().split() for _ in range(rc[0])],list(bin(int(input()))[2:])) )(list(map(int,input().split())))


# Solution
r,c = map(int,input().split())
mat = [input().split() for _ in range(r)]
n = list(bin(int(input()))[2:])
count = 0
for row in mat:
    count += sum([1 for i in range(c - len(n) +1 ) if row[i:i+len(n)] == n])
for row in map(list,zip(*mat)):
    count += sum([1 for i in range(r - len(n) +1 ) if row[i:i+len(n)] == n])
print(count)