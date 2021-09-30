// ReCreate Array Values
// An integer sequence contains integers from X to Y. X is denoted by 1 as its the beginning value. X+1 is denoted by 2 and so on. Y is denoted by Y-X+1.
// The denoted values are passed as the input and the function recreateArr must populate the sequence values in the array.

// Please implement the function recreateArr so that the program executes successfully.

// Boundary Condition(s):
// 1 <= X, Y <= 10^5
// X < Y

// Input Format:
// The first line contains X and Y separated by a space.
// The second line contains Y-X+1 integer values.

// Output Format:
// The first line contains Y-X+1 integer values separated by a space.

// Example Input/Output 1:
// Input:
// 12 15
// 4 1 3 2

// Output:
// 15 12 14 13

// Explanation:
// 12 is denoted by 1, 13 by 2, 14 by 3 and 15 by 4.

// Example Input/Output 2:
// Input:
// 5 10
// 4 6 2 1 3 5

// Output:
// 8 10 6 5 7 9



#include <stdio.h>
#include <stdlib.h>
void recreateArr(int *arr, int X, int Y)
{
    for(int i=0;i<=Y-X;i++) arr[i]+=X-1;
}
int main()
{
    int X, Y;
    scanf("%d %d", &X, &Y);
    if(X < 1 || X > 100000)
    {
        printf("X not in range");
    }
    if(Y <= X || Y > 100000)
    {
        printf("Y not in range");
    }
    int N = Y - X + 1;
    int arr[N];
    for(int index = 0; index < N; index++)
    {
        scanf("%d", arr+index);
        if(arr[index] < 1 || arr[index] > (Y-X+1))
        {
            printf("Each integer value not in range");
        }
    }
    recreateArr(arr, X, Y);
    for(int index = 0; index < N; index++)
    {
        printf("%d ", *(arr+index));
    }
    return 0;
}
