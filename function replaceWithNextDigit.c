// function replaceWithNextDigit
// The function/method replaceWithNextDigit accepts an argument N representing an integer value.

// The function/method replaceWithNextDigit must print the output based on the following conditions.
// - For each digit D in the integer N, the program must form a new integer by replacing the digit with its next digit (for the digit 9, consider 0 as the next digit).
// - Then the program must print the resulting integers in sorted order.

// Your task is to implement the function replaceWithNextDigit so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 12543

// Output:
// 12544 12553 12643 13543 22543

// Explanation:
// For the 1st digit: 12543 -> 22543
// For the 2nd digit: 12543 -> 13543
// For the 3rd digit: 12543 -> 12643
// For the 4th digit: 12543 -> 12553
// For the 5th digit: 12543 -> 12544
// So the resulting 5 integers are printed in sorted order.
// 12544 12553 12643 13543 22543

// Example Input/Output 2:
// Input:
// 860679

// Output:
// 860670 860689 860779 861679 870679 960679

// Example Input/Output 3:
// Input:
// 999

// Output:
// 99 909 990












#include <stdio.h>
#include <stdlib.h>
void replaceWithNextDigit(int N)
{
    int x;
    char temp[100001];
    sprintf(temp,"%d",N);
    int len=strlen(temp);
    int arr[len];
    for(int i=0;i<len;i++){
        char each[len];
        sprintf(each,"");
        for(int j=0;j<len;j++){
            if(i==j){
                x = temp[j] - 47 ;
                if(x==10) x =0 ;
                sprintf(each,"%s%d",each,x);
                
            }else{
                sprintf(each,"%s%c",each,temp[j]);
            }
        }
        arr[i]=atoi(each);
    }
    for(int i=0;i<len;i++){
        for(int j=i+1;j<len;j++){
            if(arr[i]>arr[j]){
                int t = arr[i];
                arr[i] = arr[j];
                arr[j] = t;
            }
        }
    }
    for(x=0;x<len;x++){
        printf("%d ",arr[x]);
    }
}
int main()
{
    int N;
    scanf("%d", &N);
    replaceWithNextDigit(N);
    return 0;
}