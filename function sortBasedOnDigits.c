// function sortBasedOnDigits
// The function/method sortBasedOnDigits accepts two arguments SIZE and arr. The integer SIZE represents the size of the integer array arr.

// The function/method sortBasedOnDigits must sort the integers in the given array based on digits starting from the most significant digit.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 6
// 200 2 22 32 3 4

// Output:
// 2 200 22 3 32 4

// Explanation:
// Here N=6 and the given 6 integers are 200 2 22 32 3 4.
// After sorting the given array based on digits starting from the most significant digit, the array becomes 2 200 22 3 32 4.

// Example Input/Output 2:
// Input:
// 5
// 124 1201 204 230 104

// Output:
// 104 1201 124 204 230









#include <stdio.h>
#include <stdlib.h>
void sortBasedOnDigits(int SIZE, int *arr)
{
    int i,j;
    for(i=0;i<SIZE;i++){
        for(j=i+1;j<SIZE;j++){
            char a[9999], b[9999];
            sprintf(a,"%d",arr[i]);
            sprintf(b,"%d",arr[j]);
            if(strcmp(a,b)>0){
                int t = arr[i];
                arr[i] = arr[j];
                arr[j] = t;
            }
            
        }
    }
}
int main()
{
    int N;
    scanf("%d", &N);
    int arr[N];
    for(int index = 0; index < N; index++)
    {
        scanf("%d", &arr[index]);
    }
    sortBasedOnDigits(N, arr);
    for(int index = 0; index < N; index++)
    {
        printf("%d ", arr[index]);
    }
    return 0;
}