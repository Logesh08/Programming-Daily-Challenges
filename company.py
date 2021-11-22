s=input().strip()
ans=1
for i in range(len(s)-1):
    c=s[i]
    if c in '012' and int(s[i+1])<7:
        ans+=1
print(len(ans))