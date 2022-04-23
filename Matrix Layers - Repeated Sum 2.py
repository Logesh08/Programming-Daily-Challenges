# Matrix Layers - Repeated Sum
# The program must accept an integer matrix of size N*N as the input. The program must find the sum of integers in each layer of the matrix (from outer layer to inner layer). Then the program must print the repeated sum among the obtained sum values. If two or more sum values are repeated, then the program must print the first occurring sum as the output. If there is no repeated sum, then the program must print -1 as the output.

# Boundary Condition(s):
# 3 <= N <= 50
# 0 <= Matrix element value <= 1000

# Input Format:
# The first line contains N.
# The next N lines each contain N integers separated by a space.

# Output Format:
# The first line contains an integer representing the repeated sum or -1 based on the given conditions.

# Example Input/Output 1:
# Input:
# 5
# 2 3 4 5 1
# 3 10 6 7 2
# 4 13 6 9 2
# 5 6 5 3 3
# 7 5 7 2 4

# Output:
# 59

# Explanation:
# 1st layer sum: 59
# 2nd layer sum: 59
# 3rd layer sum: 6
# Here the sum 59 is repeated, so 59 is printed as the output.

# Example Input/Output 2:
# Input:
# 7
# 76 56 96 69 12 75 81
# 76 69 64 95 57 62 53
# 84 32 64 24 18 51 10
# 99 8 64 22 12 88 23
# 52 94 28 93 43 95 97
# 40 1 91 8 56 84 50
# 76 65 20 87 97 45 80

# Output:
# -1

# Example Input/Output 3:
# Input:
# 8
# 1 1 1 1 1 1 1 1
# 1 2 2 2 2 2 2 1
# 1 1 1 1 1 1 2 1
# 1 1 1 3 3 1 2 1
# 1 1 1 3 3 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1

# Output:
# 28














n=int(input())
li=[[int(i) for i in input().split()] for j in range(n)]
li2=[]
for k in range(n//2):
    x=0
    for j in range(k,n-k):
        x+=li[k][j]
    for j in range(n-k-1,k-1,-1):
        x+=li[-(k+1)][j]
    for i in range(k+1,n-k-1):
        x+=li[i][k]+li[i][-(k+1)]
    li2.append(x)
if n%2!=0:
    li2.append(li[n//2][n//2])
for i in li2:
    if li2.count(i)>1:
        print(i)
        exit()
print(-1)