<h2>Python - C 008</h2>
Please convert the following python code to c so that the c program executes successfully passing the test cases.
<br/>
<br/>
<pre>
#include <stdio.h>
#include <math.h>
void main(){
    int f,s,k,i;
    scanf("%d%d%d",&f,&s,&k);
    int a[99999],b[99999];
    int aind,bind;
    while(f>0){
        a[aind++]=f%2;
        f/=2;
    }
    while(s>0){
        b[bind++]=s%2;
        s/=2;
    }
    int p=k*2 - 1;
    int d=0;
    for(i=aind-1;i>=aind-k;i--){
        int t = pow(2,p--);
        d += a[i] * t;
    }
    for(i=k-1;i>=0;i--){
        int t = pow(2,p--);
        d += b[i] * t;
    }
    printf("%d",d);
    return 0;
}
</pre>