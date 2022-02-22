// function getIntegersWithSameEnds
// The function/method getIntegersWithSameEnds accepts two arguments str and K. The first argument str represents a string value containing only digits. The second argument K represents an integer value.

// The function/method getIntegersWithSameEnds must form all possible K-digit integers with the same ends using the consecutive digits in the given string. Then the program must return an array of integers containing the resulting K-digit integers in sorted order. If there is no such K-digit integer, then the function must return an array of size 1 with the value as -1.

// Note: K-digit integers do not have leading zeroes.

// Your task is to implement the function getIntegersWithSameEnds so that it passes all the test cases.

// The following structure is used to represent the boundedArray and is already defined in the default code (Do not write this definition again in your code).
// typedef struct BoundedArray
// {
//     int SIZE;
//     int *arr;
// } boundedArray;
// IMPORTANT: Do not write the main() function as it is already defined.

// Boundary Condition(s):
// 1 <= Length of S <= 100
// 2 <= K <= 9

// Example Input/Output 1:
// Input:
// 508562102042022
// 4

// Output:
// 2022 2042 2102 5085

// Explanation:
// Here K = 4.
// The 4-digit integers with the same ends that can be formed from the string are given below.
// 5085, 2102, 2042 and 2022
// After sorting the 4-digit integers, the integers become
// 2022 2042 2102 5085

// Example Input/Output 2:
// Input:
// 909086733834444
// 3

// Output:
// 383 444 444 909

// Example Input/Output 3:
// Input:
// 909086733834
// 5

// Output:
// -1











#include <stdio.h>
#include <stdlib.h>
typedef struct BoundedArray
{
    int SIZE;
    int *arr;
} boundedArray;
boundedArray* getIntegersWithSameEnds(char *str, int K)
{
    boundedArray *barr = malloc(99999999);
    barr->arr = malloc(9999999);
    // barr-> SIZE = 0;
    int i=0,ind=0,kind=0;
    int arr[strlen(str)];
    if(strlen(str)<K){
        barr->arr[0]=-1;
        barr->SIZE = 1;
        return barr;
    }
    
    for(;i<=strlen(str)-K;i++){
        char temp[K+2];
        int tid=0;
        if(str[i]==str[i+K-1] && str[i]!='0'){
            for(int j=i;j<=i+K-1;j++){
                temp[tid++]=str[j];
            }
            temp[tid]='\0';
            // printf("%s\n",temp);
            barr->arr[kind++]=atoi(temp);
        }
    }
    if(kind<=0){
        barr->arr[0]=-1;
        barr->SIZE = 1;
        return barr;
    }
    // barr->arr[0]=69;
    for (int i = 0; i < kind; i++) {     
        for (int j = i+1; j < kind; j++) {     
           if(barr->arr[i] > barr->arr[j]) {    
               int temp = barr->arr[i];    
               barr->arr[i] = barr->arr[j];    
               barr->arr[j] = temp;    
           }     
        }     
    }    
    barr->SIZE = kind;
    return barr;
}




int main()
{
    char str[101];
    int K;
    scanf("%s\n%d", str, &K);
    boundedArray *bArr = getIntegersWithSameEnds(str, K);
    if(bArr == NULL)
    {
        printf("Array is not formed\n");
    }
    if(bArr->SIZE <= 0)
    {
        printf("Invalid size for the array\n");
    }
    for(int index = 0; index < bArr->SIZE; index++)
    {
        printf("%d ", bArr->arr[index]);
    }
    return 0;
}
