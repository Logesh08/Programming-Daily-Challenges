# Repeated Integer Pattern

# The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

# Boundary Condition(s):
# 1 <= N <= 50

# Input Format:
# The first line contains N.

# Output Format:
# The lines contain the desired pattern as shown in the Example Input/Output section.

# Example Input/Output 1:
# Input:
# 4

# Output:
# 1 2 3 4
# 1 2 2 3 4
# 1 2 3 3 3 4
# 1 2 3 4 4 4 4

# Example Input/Output 2:
# Input:
# 5

# Output:
# 1 2 3 4 5
# 1 2 2 3 4 5
# 1 2 3 3 3 4 5
# 1 2 3 4 4 4 4 5
# 1 2 3 4 5 5 5 5 5



# Max Execution Time Limit: 1000 millisecs





n = int(input())
for i in range(1,n+1):
    arr = []
    for j in range(1,n+1):
        if i==j:
            [arr.append(i) for i in [j]*j]
        else:
            arr.append(j)
    print(*arr,sep=' ')
    
    
    
# OneLiner
[(lambda n: [print(*(i if i == j else j for j in range(1, n + 1)), sep=' ') for i in range(1, n + 1)])(int(input()))]