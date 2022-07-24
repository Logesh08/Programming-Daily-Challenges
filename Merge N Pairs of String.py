# Merge N Pairs of String

# The program must accept an integer N and N pairs of strings. Then the program must merge every pair of strings and print the merged string.

# Boundary Condition(s):
# 2 <= N <= 100
# 1 <= Length of String <= 1000

# Input Format:
# The first line contains N.
# The next N lines contain two strings each.

# Output Format:
# The first N lines contain the merged strings.

# Example Input/Output 1:
# Input:
# 2
# good bye
# take care

# Output:
# gboyoed
# tcaakree

# Example Input/Output 2:
# Input:
# 3
# cool buddy
# think well
# welcome tin

# Output:
# cbouodldy
# twheilnlk
# wteilncome






n = int(input())
arr = [list(map(list,input().split())) for i in range(n)]
for pairs in arr:
    while pairs[0] or pairs[1]:
        if pairs[0]: print(pairs[0].pop(0),end='')
        if pairs[1]: print(pairs[1].pop(0),end='')
    print()