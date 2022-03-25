# First Non-Repeated Submatrix
# The program must accept a character matrix of size R*C and an integer K as the input. The values of R and C are always divisible by K. The program must print the first non-repeated K*K submatrix in the given matrix as the output. If there is no such submatrix, then the program must print -1 as the output.

# Boundary Condition(s):
# 4 <= R, C <= 50
# 2 <= K <= 25

# Input Format:
# The first line contains R and C separated by a space.
# The next R lines, each contains C characters separated by a space.
# The R+2nd line contains K.

# Output Format:
# The first K lines contain the first non-repeated K*K submatrix in the given matrix or the first line contains -1.

# Example Input/Output 1:
# Input:
# 6 9
# a b c l m n a b c
# d e f p q r d e f
# g h i x z y g h i
# c b a c b a n m l
# f e d f e d r q p
# i h g i h g y z x
# 3

# Output:
# l m n
# p q r
# x z y

# Explanation:
# Here R=6, C=9 and K=3.
# The first non-repeated 3*3 submatrix is highlighted below.
# a b c l m n a b c
# d e f p q r d e f
# g h i x z y g h i
# c b a c b a n m l
# f e d f e d r q p
# i h g i h g y z x

# Example Input/Output 2:
# Input:
# 4 4
# a b c d
# e f g h
# c d a b
# g h e f
# 2

# Output:
# -1





r,c = map(int,input().split())
mat = [input().split() for _ in range(r)]
k = int(input())
subMat = []
for i in range(0,r,k):
    for j in range(0,c,k):
        t = ''
        for x in range(i,i+k):
            for y in range(j,j+k):
                t+=mat[x][y]
        subMat.append(t)
for i in subMat:
    if subMat.count(i) == 1:
        i = list(i)
        for _ in range(k):
            for _ in range(k):
                print(i.pop(0),end=' ')
            print()
        exit()
print(-1)