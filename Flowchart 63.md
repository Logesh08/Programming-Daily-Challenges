<img src="./src/PID14837.png"/>

<pre>
m,n = map(int,input().split())
while m&lt;n:
    print(m,end=' ')
    if n%10!=0 and n%2!=0:
        m+=n%10
    else:
        m+=1
    n-=1
</pre>