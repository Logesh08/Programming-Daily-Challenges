<img src="./src/PID15061.png"/>

<pre>
n,a,b,c = map(int,input().split())
val = ctr = 1
while ctr &lt;= n:
    print(val,end=' ')
    if val == a:
        val = b
    elif val == c:
        val = 0
    val += 1
    ctr += 1
</pre>