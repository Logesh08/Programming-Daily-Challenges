// function getSumOrString
// The function/method getSumOrString accepts an argument str. The string str contains the integer values separated by a space or the alphabets separated by a space.

// The function/method getSumOrString must return a string value based on the following conditions.
// - If the string str contains integers, then the function must return their sum as a string.
// - Else the function must form a string by concatenating the alphabets and return the string.

// Your task is to implement the function getSumOrString so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 12 45 7 -200 6100

// Output:
// 5964

// Explanation:
// The given string contains the integer values separated by a space.
// 12 + 45 + 7 + (-200) + 6100 = 5964.

// Example Input/Output 2:
// Input:
// S k i l l R a c k

// Output:
// SkillRack

// Explanation:
// The given string contains the alphabets separated by a space.
// S k i l l R a c k -> SkillRack.






#include <stdio.h>
#include <stdlib.h>

#include<string.h>
char* getSumOrString(char *str)
{
    char * res = malloc(10000001);
    if(tolower(str[0])>='a' && tolower(str[0])<='z'){
        int i=0,ind=0;
        for(;i<strlen(str);i+=2){
            res[ind++] = str[i];
        }
    }else{
        int sum = 0;
        char *token = strtok(str," ");
        while(token!=NULL){
            sum+=(atoi(token));
            token = strtok(NULL," ");
        }
        sprintf(res,"%d",sum);
    }
    return res;
}



int main()
{
    char str[101];
    scanf("%[^\n\r]", str);
    char *result = getSumOrString(str);
    if(result == NULL || result == str)
    {
        printf("String is not formed\n");
    }
    if(result[0] == '\0' || result[0] == ' ')
    {
        printf("String is empty\n");
    }
    printf("%s", result);
    return 0;
}