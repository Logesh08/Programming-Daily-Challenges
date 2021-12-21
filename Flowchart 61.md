<img src="./src/PID14922.png"/>

<pre>
x,y=map(int,input().split())
while x<y:
    print(x,y)
    if x%2==y%2:
        x+=1
        y-=2
    else:
        x+=2
        y-=1
</pre>