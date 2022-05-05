// Electronic Display - Maximum Value
// In a four-digit electronic display, each digit is displayed using seven segments. The program must accept an integer N representing the number of segments to display an integer X. The program must print the maximum possible four-digit integer X that can be displayed using N segments as the output.
// The number of segments required to display each digit is given below.
// 0 - 6
// 1 - 2
// 2 - 5
// 3 - 5
// 4 - 4
// 5 - 5
// 6 - 6
// 7 - 3
// 8 - 7
// 9 - 6

// Boundary Condition(s):
// 8 <= N <= 28

// Input Format:
// The first line contains N.

// Output Format:
// The first line contains X.

// Example Input/Output 1:
// Input:
// 13

// Output:
// 9711

// Explanation:
// Here N = 13.
// The maximum possible four-digit integer that can be displayed using 13 segments is 9711 (9+7+1+1 = 13).

// Example Input/Output 2:
// Input:
// 10

// Output:
// 7711

// Example Input/Output 3:
// Input:
// 18

// Output:
// 9977







#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n;
    scanf("%d",&n);
    int a[]={6,2,5,5,4,5,6,3,7,6};
    for(int i = 9999;i>=1000;i--){
        int x=i,s=0;
        while(x){
            int r=x%10;
            s+=a[r];
            x/=10;
        }
        if(n==s){
            printf("%d",i);
            return 0;
        }
    }
}