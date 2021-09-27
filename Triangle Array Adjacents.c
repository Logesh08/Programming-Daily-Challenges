// Triangle Array Adjacents
// An array of N integers is passed as the input. The program must print how many triangles T can be formed using the adjacent values in the array.

// Note: A triangle can be formed with side lengths a, b and c if a+b > c and a+c > b and b+c > a.

// Boundary Condition(s):
// 3 <= N <= 100
// 1 <= Each integer value <= 10^4

// Input Format:
// The first line contains N.
// The second line contains the N integer values.

// Output Format:
// The first line contains T.

// Example Input/Output 1:
// Input:
// 4
// 4 5 3 9

// Output:
// 1

// Explanation:
// 4 5 3 can form a triangle.
// 5 3 9 cannot form a triangle.

// Example Input/Output 2:
// Input:
// 4
// 4 5 3 6

// Output:
// 2

// Example Input/Output 3:
// Input:
// 5
// 11 11 11 11 10

// Output:
// 3

// Example Input/Output 4:
// Input:
// 5
// 1 2 5 7 22

// Output:
// 0




#include<stdio.h>

int main() {
    int n,i,formableCount=0;
    scanf("%d\n",&n);
    int arr[n];
    for(i=0;i<n;i++){
        scanf("%d ",&arr[i]);
    }
    for(i=0;i<n-2;i++){
        int a=arr[i],b=arr[i+1],c=arr[i+2];
        if(a+b > c && a+c > b && b+c > a){
            formableCount+=1;
        }
    }
    printf("%i", formableCount);
}
