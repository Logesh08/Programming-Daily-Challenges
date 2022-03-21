// function removeReversedWords
// The function/method removeReversedWords accepts two arguments str1 and str2 representing two string values. The string str1 contains multiple words separated by a space. The string str2 contains exactly one word.

// The function/method removeReversedWords must remove all the occurrences of the word str2 and its reverse in the string str1. Then the function must return the revised string as a new string. If the string becomes empty, then the function must return -1 as a string.

// Your task is to implement the function removeReversedWords so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// nightingale lion tiger mosquito noil cockroach lion fox panda lizard
// lion

// Output:
// nightingale tiger mosquito cockroach fox panda lizard

// Explanation:
// After removing all the occurrences of "lion" and its reverse in the first string, the string becomes
// nightingale tiger mosquito cockroach fox panda lizard

// Example Input/Output 2:
// Input:
// monkey monkey yeknom monkey yeknom
// yeknom

// Output:
// -1



#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char* removeReversedWords(char *str1, char *str2)
{
    char *ret = malloc(999999);
    char rev[strlen(str2)+1];
    rev[strlen(str2)] = '\0';
    int ind =0;
    for(int i=strlen(str2)-1;i>=0;i--){
        rev[ind++] = str2[i];
    }
    char *token = strtok(str1," ");
    while(token){
        if(strcmp(rev,token)!=0 && strcmp(str2,token)!=0){
            sprintf(ret,"%s %s",ret,token);
        }
        token = strtok(NULL," ");
    }
    if(strcmp(&ret[1],"\0")!=0) {
        return &ret[1] ;
    }
    else{
        strcpy(ret,"-1");
        return ret;
    }
}

int main()
{
    char str1[1001], str2[1001];
    scanf("%[^\n\r]\n\r%s", str1, str2);
    char *result = removeReversedWords(str1, str2);
    if(result == NULL || result == str1 || result == str2)
    {
        printf("String is not formed\n");
    }
    if(result[0] == ' ' || result[0] == '\0')
    {
        printf("String is empty\n");
    }
    printf("%s", result);
    return 0;
}