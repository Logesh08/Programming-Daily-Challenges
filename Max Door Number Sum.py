# Max Door Number Sum
# There is a town in which H houses are situated in each of the S streets. Each house has a door number which is an positive integer. So these S*H door numbers form a matrix.

# From any house you can navigate to the house in the east(right) or to the house located south (bottom). Thus the navigation ends when there is no house in the east or in the south.

# The program must print the maximum possible sum of the door numbers traversed during the above mentioned navigation.

# Input Format:
# The first line will S and H separated by a space.
# Next S lines will each contain H positive integer values (representing the door numbers) separated by a space.

# Output Format:
# The first line will contain the maximum possible sum of the door numbers traversed.

# Boundary Conditions:
# 2 <= S,H <= 500
# 1 <= DoorNumber <= 10000

# Example Input/Output 1:
# Input:
# 3 3
# 15 25 30
# 45 25 60
# 70 75 10

# Output:
# 215

# Explanation:
# The maximum possible sum of 215 is obtained when we follow 15->45->70->75->10

# Example Input/Output 2:
# Input:
# 4 4
# 4 10 10 4
# 4 9 9 4
# 2 2 10 1
# 9 9 2 7

# Output:
# 52

# Explanation:
# The maximum possible sum of 52 is obtained when we follow 4->10->10->9->10->2->7





s,h=map(int,input().split())
m=[list(map(int,input().split())) for _ in range(s)]
for j in range(1,h):
    m[0][j]+=m[0][j-1]
for i in range(1,s):
    m[i][0]+=m[i-1][0]
for i in range(1,s):
    for j in range(1,h):
        m[i][j]+=max(m[i-1][j],m[i][j-1])
print(m[-1][-1])