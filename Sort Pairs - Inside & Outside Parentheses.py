# Sort Pairs - Inside & Outside Parentheses
# The program must accept N pairs of integers as the input. One of the two integers in each pair is enclosed within a pair of parentheses. The program must sort the integers that present inside the parentheses in ascending order and sort the integers that present outside the parentheses in descending order. Finally, the program must print N revised pairs as the output.

# Boundary Condition(s):
# 2 <= N <= 100
# 1 <= Each integer value <= 10^5

# Input Format:
# The first line contains N.
# The second line contains N pairs of integers separated by a space.

# Output Format:
# The first line contains the revised N pairs of integers separated by a space.

# Example Input/Output 1:
# Input:
# 4
# 12(52) (25)50 (35)10 44(60)

# Output:
# 50(25) (35)44 (52)12 10(60)

# Explanation:
# Here N = 4.
# The 4 integers that present inside the parentheses are 52, 25, 35 and 60.
# The 4 integers that present outside the parentheses are 12, 50, 10 and 44.
# After sorting those integers in the pairs based on the given conditions, the pairs become
# 50(25) (35)44 (52)12 10(60)

# Example Input/Output 2:
# Input:
# 3
# 626(564) (343)752 (179)99

# Output:
# 752(179) (343)626 (564)99




n=int(input())
s = input().strip()
a,b=[],[]
copy = s.replace("("," ").replace(")"," ").split()
s = s.split()
for i in range(n):
    if s[i][0]=="(":
        a.append(int(copy[i*2]))
        b.append(int(copy[(i*2)+1]))
    else:
        a.append(int(copy[(i*2)+1]))
        b.append(int(copy[i*2]))
a.sort();b.sort(reverse=True)
for i in range(n):
    if s[i][0]=="(":
        print("(",a[i],")",b[i],sep="",end=" ")
    else:
        print(b[i],"(",a[i],")",sep="",end=" ")