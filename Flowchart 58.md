<img src="./src/PID14866.png"/>

<pre>
x,y=map(int,input().split())
string='abcde'
ctr=1
while ctr<=x:
    ind=0
    while ind&lt;y:
        print(str(ctr)+&sbquo;.&sbquo;+string[ind%5])
        ind+=1
    ctr+=1
</pre>