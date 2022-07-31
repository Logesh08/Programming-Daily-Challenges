# Butterfly Pattern

# Accept an odd integer N as the input. 
# The program must print the pattern as shown in the Example Input/ Output section.

# Boundary Condition(s):
# 1 <= N <= 49

# Input Format:
# The first line contains the value of odd integer N.

# Output Format:
# The first N lines contain the desired pattern.

# Example Input/ Output 1:
# Input:
# 5

# Output:
# 1-2-3---3-2-1
# ---5-4-4-5
# ------0
# ---2-1-1-2
# 3-4-5---5-4-3

# Example Input/ Output 2:
# Input:
# 3

# Output:
# 1-2-2-1
# ---0
# 2-1-1-2






n = int(input())
cur = 1
count = n // 2 + 1
mc = (n // 2 - 1) * 2 + 1
rev = False
for i in range(n // 2):
    # (i * 3 * '-') + '-'.join()
    nex = cur + count;
    nums = list(map(str, range(cur, nex)))
    if rev:
        nums = nums[::-1]
    print((i * 3 * '-') + '-'.join(nums) + ('-' * (mc - i * 2)) + '-'.join(nums[::-1]))
    rev = not rev
    count -= 1
    cur = nex
print('-' * (n // 2 * 3) + '0')
cur = 1
count += 1
rev = True
for i in range(n // 2 - 1, -1, -1):
    nex = cur + count
    nums = list(map(str, range(cur, nex)))
    if rev:
        nums = nums[::-1]
    print((i * 3 * '-') + '-'.join(nums) + ('-' * (mc- i * 2)) + '-'.join(nums[::-1]))
    rev = not rev
    count += 1
    cur = nex
    