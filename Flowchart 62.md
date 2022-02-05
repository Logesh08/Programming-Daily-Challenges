<img src="./src/PID14804.png"/>

<pre>
x,y=map(int,input().split())
while True:
    n=int(input())
    if n%2==0:
        n+=x
        y-=1
    else:
        n+=y
        x-=1
    print(n,end=' ')
    if n&gt;0: continue
    else: break
</pre>