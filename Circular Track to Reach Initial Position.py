# Circular Track to Reach Initial Position

# A circular track has N positions numbered from 1 to N. The initial position I of the player and an integer M are given as the input. The player jumps M positions per move. The program must print the minimum number of moves required to reach the initial position again.

# Boundary Condition(s):
# 1 <= N <= 1000
# 1 <= I <= N
# 1 <= M <= 1000

# Input Format:
# The first line contains the value of N, I and M.

# Output Format:
# The first line contains the number of moves.

# Example Input/Output 1:

# Input:
# 10 2 5

# Output:
# 2

# Explanation:
# 2->7->2

# Example Input/Output 2:

# Input:
# 70 15 12

# Output:
# 35






n,i,m = map(int,input().split())
count,r = 1,i
i += m 
if i>n:
    i -= n 
while i!=r:
    i += m 
    count += 1
    if i>n:
        i -= n 
print(count)