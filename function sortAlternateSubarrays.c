// function sortAlternateSubarrays
// The function/method sortAlternateSubarrays accepts three arguments SIZE, arr and K. The integer SIZE represents the size of the integer array arr and the integer K represents the size of the subarray.

// The function/method sortAlternateSubarrays must sort the integers in the alternate subarrays of size K in ascending order.

// Note: The number of integers in the given array is always divisible by K.

// Your task is to implement the function sortAlternateSubarrays so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 9
// 3 2 1 5 4 6 7 9 8
// 3

// Output:
// 1 2 3 5 4 6 7 8 9

// Explanation:
// Here N=9 and K=3.
// The integers in the 1st subarray are 3, 2 and 1.
// After sorting the 1st subarray, the subarray becomes 1, 2 and 3.
// The integers in the 3rd subarray are 7, 9 and 8.
// After sorting the 3rd subarray, the subarray becomes 7, 8 and 9.

// Example Input/Output 2:
// Input:
// 8
// 70 24 36 29 68 36 92 12
// 4

// Output:
// 24 29 36 70 68 36 92 12







#include <stdio.h>
#include <stdlib.h>
void sortAlternateSubarrays(int SIZE, int *arr, int K)
{
     for(int i=0;i<SIZE;i+=K)
     {
         for(int j=i;j<i+K;j++)
         {
             for(int l=j+1;l<i+K;l++)
             {
                 if(arr[j]>arr[l])
                 {
                     int t=arr[j];
                     arr[j]=arr[l];
                     arr[l]=t;
                 }
             }
         }
         i+=K;
     }
}
int main()
{
    int N, K;
    scanf("%d", &N);
    int arr[N];
    for(int index = 0; index < N; index++)
    {
        scanf("%d", &arr[index]);
    }
    scanf("%d", &K);
    sortAlternateSubarrays(N, arr, K);
    for(int index = 0; index < N; index++)
    {
        printf("%d ", arr[index]);
    }
    return 0;
}