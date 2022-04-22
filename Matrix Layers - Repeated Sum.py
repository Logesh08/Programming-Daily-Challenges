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
mat = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
i = j = 0
r = 0
c = 1
Sum = 0
START = 0
arr = []
while True:
    if not visited[i][j]:
        visited[i][j] = 1
        Sum += mat[i][j]
        i += r 
        j += c 
        
    else:
        arr.append(Sum)
        Sum = 0
        i+=1 
        j+=1
        try:
            if not visited[i][j]:
                n -= 1 
                START += 1
            else:
                break
        except:
            break
    if j==n:
        c=0
        r=1
        j -= 1
        i += 1
    elif i==n:
        c = -1
        r = 0
        i -= 1
        j -= 1
    elif j<START:
        c = 0
        r = -1
        j += 1
        i -= 1
    elif i<START:
        r = 0
        c = 1
        i += 1
        j+=1
for i in range(len(arr)):
    if arr[i] in arr[i+1:]:
        print(arr[i])
        exit()
print(-1)
