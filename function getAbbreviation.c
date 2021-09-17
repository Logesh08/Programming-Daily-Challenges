// function getAbbreviation
// The function/method getAbbreviation accepts an argument str representing a string value which contains multiple words.

// The function/method getAbbreviation must find the abbreviation for the given words by concatenating the first alphabet of each word. Then the function must return the abbreviated string, where all the alphabets must be in upper case.

// Your task is to implement the function getAbbreviation so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// Automated teller machine

// Output:
// ATM

// Explanation:
// Here the given string is Automated teller machine.
// After concatenating the first alphabet of each word in upper case, the abbreviated string becomes ATM.

// Example Input/Output 2:
// Input:
// Laughing Out Loud

// Output:
// LOL

// Example Input/Output 3:
// Input:
// For Life and Beyond

// Output:
// FLAB


#include <stdio.h>
#include <stdlib.h>

char* getAbbreviation(char *str)
{
    char *abrv=malloc(sizeof(char*)*strlen(str));
    abrv[0]=toupper(str[0]);
    int abrIndex=1;
    for(int i=1;i<strlen(str);i++){
        if(str[i-1]==' ' && str[i]!=' '){
            abrv[abrIndex++]=toupper(str[i]);
        }
    }
    return abrv;
}


int main()
{
    char str[1001];
    scanf("%[^\n]", str);
    char *abbreviation = getAbbreviation(str);
    if(abbreviation == str)
    {
        printf("New string is not formed\n");
    }
    if(abbreviation[0] == '\0')
    {
        printf("String is empty");
    }
    printf("%s", abbreviation);
    return 0;
}