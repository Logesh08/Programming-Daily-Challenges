// function sortSubstrings
// The function/method sortSubstrings accepts two arguments str and K. The str represents a string value whose length is always divisible by the integer K.

// The function/method sortSubstrings must split the given string into substrings of equal length K. Then the function must sort the substrings and return them.

// Your task is to implement the function sortSubstrings so that the program runs successfully.

// The following structure is used to represent the boundedArray and is already defined in the default code (Do not write this definition again in your code).
// typedef struct BoundedArray
// {
//     int SIZE;
//     char **words;
// } boundedArray;

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// skillrack
// 3

// Output:
// ack llr ski

// Explanation:
// Here K = 3.
// After dividing the given string skillrack into substrings of length 3, the substrings are ski, llr and ack.
// So they are printed in sorted order.

// Example Input/Output 2:
// Input:
// internationalairport
// 4

// Output:
// inte iona lair port rnat








#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct BoundedArray
{
    int SIZE;
    char **words;
} boundedArray;


boundedArray* sortSubstrings(char *str, int K)
{
    boundedArray *barr = malloc(999999);
    
    char temp[K+1];
    int ind=0,t=0,i=0;
    barr->words = malloc(999999);
    while(str[i]!='\0'){
        temp[t++] = str[i];
        i++;
        if(i%K==0){
            temp[t] = '\0';
            barr->words[ind] = malloc(999999);
            strcpy(barr->words[ind++],temp);
            t=0;
        }
    }
    for(i=0;i<ind;i++){
        for(t=i+1;t<ind;t++){
            if(strcmp(barr->words[i],barr->words[t])>0){
                strcpy(temp,barr->words[i]);
                strcpy(barr->words[i],barr->words[t]);
                strcpy(barr->words[t],temp);
            }
        }
    }
    barr->SIZE = ind;
    return barr;
}

int main()
{
    char str[101];
    int K;
    scanf("%s\n%d", str, &K);
    boundedArray *bArr = sortSubstrings(str, K);
    if(bArr == NULL || bArr->SIZE == 0 || bArr->words == NULL
            || bArr->words[0][0] == '\0' || bArr->words[0][0] == ' ')
    {
        printf("String values are not formed\n");
    }
    for(int index = 0; index < bArr->SIZE; index++)
    {
        printf("%s ", bArr->words[index]);
    }
    return 0;
}



