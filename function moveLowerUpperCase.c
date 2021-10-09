// function moveLowerUpperCase
// The function/method moveLowerUpperCase accepts an argument str representing a string value (without any spaces).

// The function/method moveLowerUpperCase must move all the lower case alphabets to the beginning and all the upper case alphabets to the end. Then the function must return the modified string value as a new string.

// Your task is to implement the function moveLowerUpperCase so that the program runs successfully.

// IMPORTANT: Do not implement the main() function as it is already defined.

// Boundary Condition(s):
// 1 <= Length of the string <= 1000

// Input Format:
// The first line contains the string value.

// Output Format:
// The first line contains the modified string value.

// Example Input/Output 1:
// Input:
// 5OranGesAretheRe

// Output:
// ranesrethee5OGAR

// Explanation:
// Here the given string is 5OranGesAretheRe.
// The lower case alphabets in the given string are r a n e s r e t h e e.
// The upper case alphabets in the given string are O G A R.
// After moving all the lower case alphabets to the beginning and all the upper case alphabets to the end, the string becomes ranesrethee5OGAR.

// Example Input/Output 2:
// Input:
// 5Tiger2OWL3ox1Lion6FOX

// Output:
// igeroxion52316TOWLLFOX



#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* moveLowerUpperCase(char *str)
{
    int len= strlen(str);
    char *ptr = malloc(sizeof(char)*len);
    char num[len],low[len],upper[len];
    int numIndex=0,lowIndex=0,upperIndex=0,i=0;
    while(str[i]!='\0'){
        if(isupper(str[i])){
            upper[upperIndex++]=str[i];
        }
        else if(islower(str[i])){
            low[lowIndex++]=str[i];
        }
        else{
            num[numIndex++]=str[i];
        }
        i++;
    }
    num[numIndex]=low[lowIndex]=upper[upperIndex]='\0';
    sprintf(ptr,"%s%s%s",low,num,upper);
    return ptr;
}

int main()
{
    char str[1001];
    scanf("%s", str);
    char *ptr = moveLowerUpperCase(str);
    if(str == ptr)
    {
        printf("New string is not formed\n");
    }
    if(ptr[0] == '\0')
    {
        printf("String is empty\n");
    }
    printf("%s", ptr);
}