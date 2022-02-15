// function splitStringSameCharacters
// The function/method splitStringSameCharacters accept an argument str representing a string value.

// The function/method splitStringSameCharacters must split the given string at which a character occurs exactly twice consecutively. Then the function must print the resulting words as the output.

// Your task is to implement the function splitStringSameCharacters so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// moonlighttiger

// Output:
// mo onlight tiger

// Explanation:
// Here the given string is moonlighttiger.
// The characters 'o' and 't' occur exactly twice consecutively.
// After splitting the string at which the characters occur exactly twice consecutively, the string becomes
// mo onlight tiger

// Example Input/Output 2:
// Input:
// aabbbccddddeeeeeeffgggg

// Output:
// a abbbc cddddeeeeeef fgggg






#include <stdio.h>
#include <stdlib.h>

void splitStringSameCharacters(char *str)
{
    char *ptr = malloc(9999999);
    int i = 0;
    while(str[i]!='\0'){
        printf("%c",str[i]);
        if(str[i+1]==str[i] && str[i+2]!=str[i] && str[i-1]!=str[i]){ 
            printf(" ");
        };
        i++;
    }
}

int main()
{
    char str[1001];
    scanf("%s", str);
    splitStringSameCharacters(str);
    return 0;
}