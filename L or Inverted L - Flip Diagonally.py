# L or Inverted L - Flip Diagonally
# The program must accept integer values in L-shape or inverted L-shape as the input. The program must flip the given shape diagonally and print the integers as the output. The empty spaces must be printed as asterisks.
# Note: Both the edges of L and inverted L have an equal length (i.e., an equal number of integers in both the edges).

# Input Format:
# The lines contain the integer values in L-shape or inverted L-shape.

# Output Format:
# The lines contain the integer values and asterisks based on the given conditions.

# Example Input/Output 1:
# Input:
# 1 2 3 4 5
# 6
# 7
# 8
# 9

# Output:
# * * * * 5
# * * * * 4
# * * * * 3
# * * * * 2
# 9 8 7 6 1

# Explanation:
# The integers occur in the inverted L-shape.
# So they are flipped diagonally and printed as the output.

# Example Input/Output 2:
# Input:
# 1
# 2
# 3
# 4 5 6 7

# Output:
# 1 2 3 4
# * * * 5
# * * * 6
# * * * 7

# Explanation:
# The integers occur in the L-shape.
# So they are flipped diagonally and printed as the output.






arr=[]
try:
    while True:
        arr.append(input().split())
except:
    length=len(arr)-1
    if len(arr[0])>1:
        for i in range(len(arr)-1):
            print('* '*length,arr[0][length-i],sep='')
        for i in arr[::-1]:
            print(i[0],end=' ')
    else:
        for i in arr:
            print(i[0],end=' ')
        print()
        for i in range(length):
            print('* '*length,arr[-1][i+1],sep='')