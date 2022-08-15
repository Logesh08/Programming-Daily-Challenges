# Count the Successful Withdrawals

# An ATM charges Rs. X for each withdrawal. Given initial amount A, print the maximum number of successful withdrawals as the output that can be made when Rs. Y is withdrawn each time.

# Boundary Condition(s):
# 1 <= A, X, Y <= 999999999

# Input Format:
# The first line contains the amount A, withdrawal charge X and withdrawal amount Y separated by space(s).

# Output Format:
# The first line contains the count of successful withdrawals.

# Example Input/Output 1:
# Input:
# 150 20 40

# Output:
# 2

# Example Input/Output 2:
# Input:
# 100 10 10

# Output:
# 5





a,x,y = map(int,input().split())
cnt = 0
while a>=x+y:
    a-=x+y
    cnt += 1
print(cnt,0)