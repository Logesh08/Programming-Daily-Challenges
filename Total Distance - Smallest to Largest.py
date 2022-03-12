# Total Distance - Smallest to Largest
# The program must accept an integer matrix of size R*C containing only unique integers as the input. The program must find the distance between the smallest integer and the 2nd smallest integer. Then the program must find the distance between the 2nd smallest integer and the 3rd smallest integer and so on. Finally, the program must print the total distance as the output.

# Distance between two integers X and Y in the matrix = Maximum(Absolute difference between the row positions of X and Y, Absolute difference between the column positions of X and Y).

# Boundary Condition(s):
# 2 <= R, C <= 50
# 1 <= Matrix element value <= 10^4

# Input Format:
# The first line contains R and C separated by a space.
# The next R lines, each contains C integer values separated by a space.

# Output Format:
# The first line contains an integer value representing the total distance.

# Example Input/Output 1:
# Input:
# 3 3
# 6 7 4
# 3 8 5
# 2 9 1

# Output:
# 11

# Explanation:
# Distance between 1 and 2: 2
# Distance between 2 and 3: 1
# Distance between 3 and 4: 2
# Distance between 4 and 5: 1
# Distance between 5 and 6: 2
# Distance between 6 and 7: 1
# Distance between 7 and 8: 1
# Distance between 8 and 9: 1
# Total distance = 2+1+2+1+2+1+1+1 = 11.

# Example Input/Output 2:
# Input:
# 3 4
# 50 65 60 94
# 87 12 70 44
# 21 81 40 32

# Output:
# 18







r,c=map(int,input().split())
arr = []
def dude(l):
    l=list(l)
    for i in l:
        arr.append(i)
    return l
distance=0
mat = [dude(map(int,input().split())) for _ in range(r)]
arr.sort()
for i in range(1,len(arr)):
    x,y=arr[i-1],arr[i]
    xInd,yInd=[],[]
    for i in range(r):
        if xInd != [] and yInd !=[]:
            break
        for j in range(c):
            if mat[i][j]==x:
                xInd = [i,j]
            if mat[i][j]==y:
                yInd = [i,j]
    distance+=(max([abs(xInd[0] - yInd[0]),abs(xInd[1] - yInd[1])]))
print(distance)