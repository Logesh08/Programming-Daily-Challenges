# 





s = input().strip()
n = int(input())
ctr = 1
for i in range(0,len(s),n):
    if ctr%2: print(s[i:i+n])
    ctr += 1
