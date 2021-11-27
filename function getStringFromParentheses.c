// function getStringFromParentheses
// The function/method getStringFromParentheses accepts an argument str representing a string value. The string str contains alphabets and a pair of parentheses.

// The function/method getStringFromParentheses must return a string containing all the characters between the open parenthesis and the close parenthesis in the given string. If there are no characters between the pair of parentheses, then the function must return -1 as a string value. Consider string in circular fashion when finding the characters between the open parenthesis and the close parenthesis.

// Your task is to implement the function getStringFromParentheses so that it passes all the test cases.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// abcd(SkillRack)pqrs

// Output:
// SkillRack

// Explanation:
// Here the given string value is abcd(SkillRack)pqrs.
// All the characters between the pair of parentheses are SkillRack.
// So SkillRack is printed as the output.

// Example Input/Output 2:
// Input:
// abcdef)ghij(klmno

// Output:
// klmnoabcdef

// Example Input/Output 3:
// Input:
// bank()account

// Output:
// -1

// Example Input/Output 4:
// Input:
// )donkey(

// Output:
// -1









#include <stdio.h>
#include <stdlib.h>
char* getStringFromParentheses(char *str)
{
    char* string=(char *)malloc(sizeof(char)*1001);
    int index,len=strlen(str);
    for(int i=0;i<len;i++)
    {
        if(str[i]=='(')
        {
            index=i;
            break;
        }
    }
    if(str[(index+1)%len]==')')
    {
        strcpy(string,"-1");
        return string;
    }
    for(int i=(index+1)%len,ind=0;str[i]!=')';i=(i+1)%len,ind++)
    {
        string[ind]=str[i];
    }
    return string;
}
int main()
{
    char str[101];
    scanf("%s", str);
    char *newStr = getStringFromParentheses(str);
    if(newStr == NULL || newStr == str)
    {
        printf("New string is not formed\n");
    }
    if(newStr[0] == '\0' || newStr[0] == ' ')
    {
        printf("String is empty\n");
    }
    printf("%s", newStr);
    return 0;
}