// function getConsecutiveVowels
// The function/method getConsecutiveVowels accepts an argument str representing a string value which contains only alphabets.

// The function/method getConsecutiveVowels must return an array of string values representing the consecutive vowels in the given string str. If there is no vowel in the string, then the function must return an array of size 1 with the string value "-1".

// Your task is to implement the function getConsecutiveVowels so that it passes all the test cases.

// The following structure is used to represent the boundedArray and is already defined in the default code (Do not write this definition again in your code).
// typedef struct BoundedArray
// {
//     int SIZE;
//     char **vowels;
// } boundedArray;

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// eagle

// Output:
// ea
// e

// Explanation:
// Here the given string is eagle.
// The consecutive vowels in the string eagle are ea and e.
// Hence the output is
// ea
// e

// Example Input/Output 2:
// Input:
// AbcdEIOfghIOUA

// Output:
// A
// EIO
// IOUA

// Example Input/Output 3:
// Input:
// jklmn

// Output:
// -1















#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct BoundedArray
{
    int SIZE;
    char **vowels;
} boundedArray;
int isVowel(char c){
    c=tolower(c);
    return (c=='a'||c=='e'||c=='i'||c=='o'||c=='u')?1:0;
}
boundedArray* getConsecutiveVowels(char str[])
{
    int s=0;
    boundedArray *barr = malloc(999999); 
    barr->vowels=malloc(999999);
    for(int i=0;str[i]!='\0';i++){
        char temp[9999];
        int ind=0;
        while(str[i]!='\0' && isVowel(str[i])){
            temp[ind++] = str[i];
            i++;
        }
        if(ind>0) {
            temp[ind]='\0';
            barr->vowels[s]=malloc(999999);
            strcpy(barr->vowels[s++],temp);
        }
    }
    if(s==0){
        barr->vowels[0] = malloc(999999);
        strcpy(barr->vowels[0],"-1");
        barr->SIZE = 1;
    }else{
        barr->SIZE = s;
    }
    return barr;
}
int main()
{
    char str[1001];
    scanf("%s", str);

    boundedArray *bArr = getConsecutiveVowels(str);

    if(bArr == NULL || bArr->SIZE == 0 || bArr->vowels == NULL
            || bArr->vowels[0][0] == '\0' || bArr->vowels[0][0] == ' ')
    {
        printf("String values are not formed\n");
    }
    for(int index = 0; index < bArr->SIZE; index++)
    {
        printf("%s\n", bArr->vowels[index]);
    }
    return 0;
}