# Same Characters in Zigzag Matrix

# Accept a matrix of size NxN containing only characters as input. The program must print the characters which are in the same positions in the forward and the reverse zig-zag traversal. If there is no character in the same position in such traversal then print -1 as the output. 

# Boundary Condition(s):
# 2 <= N <= 20

# Input Format:
# The first line contains the value of N.
# The next N lines contain N characters separated by space.

# Output Format:
# The first line contains the characters which are in the same positions in the forward and the reverse zig-zag traversal separated by space(s) or -1.  

# Example Input/ Output 1:
# Input:
# 5
# a b c d e
# f g h i j
# k l m n o
# f g h i j
# k r c f a

# Output:
# a c h m

# Explanation:
# In the forward traversal, the matrix contains a, b, c, d, e, j, i, h, g, f, k, l, m, n, o, j, i, h, g, f, k, r, c, f and a.
# In the reverse traversal, the matrix contains a, f,  c, r,  k, f, g, h, i, j, o, n, m, l, k, f, g, h, i, j, e, d, c, b and a.
# While traversing in the forward and reverse direction, the characters in the same positions are a, c, h and m as highlighted in blue color.

# Example Input/ Output 2:
# Input:
# 6
# m o h n g i
# t s v u h r
# g l m n n o
# o c b d f g
# r h v v s t
# o g i g f e 

# Output:
# g r h v s t g o 

# Example Input/ Output 3:
# Input:
# 4
# a b c d
# f g h i
# k l m n
# f g h i 

# Output:
# -1








n = int(input()) 
mat = [ input().split() for _ in range(n) ]  
arr = []
for i in range(n):
    for j in range(n):
        if (mat[i][-1-j if i%2 else j]==mat[-1-i][j if i%2 else -1-j]):
            arr.append(mat[i][-1-j if i%2 else j])
print(*arr[:len(arr)//2 +len(arr)%2] if arr else [-1])