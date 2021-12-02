# Rearrange Mixed Matrix
# The program must accept a matrix of size R*C as the input. The given matrix contains integers, characters and words. The program must rearrange the matrix so that all the characters occur first, all the integers occur second and all the words occur last in the matrix. Finally, the program must print the revised matrix as the output.

# Integer: It contains only digits without any leading zeroes.
# Character: All characters except the digits.
# Words: It contains two or more characters.

# Boundary Condition(s):
# 2 <= R, C <= 50
# 0 <= Each integer value in the matrix <= 10^8
# 2 <= Length of each word in the matrix <= 50

# Input Format:
# The first line contains R and C separated by a space.
# The next R lines, each contains C values separated by a space.

# Output Format:
# The first R lines, each contains C values separated by a space representing the revised matrix.

# Example Input/Output 1:
# Input:
# 4 5
# 12 74 K rock t
# 9 stone a b c
# sun moon 7 h 8
# hi3hi p 900 ab 250

# Output:
# K t a b c
# h p 12 74 9
# 7 8 900 250 rock
# stone sun moon hi3hi ab

# Explanation:
# In the given 4*5 matrix, there are 7 characters, 7 integers and 6 words.
# 7 characters -> K t a b c h p
# 7 integers -> 12 74 9 7 8 900 250
# 6 words -> rock stone sun moon hi3hi ab
# After modifying the matrix based on the given conditions, the matrix becomes
# K t a b c
# h p 12 74 9
# 7 8 900 250 rock
# stone sun moon hi3hi ab

# Example Input/Output 2:
# Input:
# 5 3
# skillrack 2020 june
# a b #
# 1 2 3
# 4c 10L K7
# H hundred 001

# Output:
# a b #
# H 2020 1
# 2 3 skillrack
# june 4c 10L
# K7 hundred 001




r,c=map(int,input().split())
arr=[]
for i in range(r):
    for val in input().split():
        arr.append(val)
def sorter(x):
    if len(x)==1 and not x.isdigit():
        return 0
    elif x.isdigit():
        if x[0]=='0' and len(x)>1:
            return 2
        return 1
    else:
        return 2
arr.sort(key=sorter)
for i in range(r):
    for j in range(c):
        print(arr.pop(0),end=' ')
    print()