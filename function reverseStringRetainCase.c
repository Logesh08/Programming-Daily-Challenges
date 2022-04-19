// function reverseStringRetainCase
// The function/method reverseStringRetainCase accepts an argument str representing a string value that contains multiple words.

// The function/method reverseStringRetainCase must reverse each word in the given string, but the case of the alphabets must be retained in their positions.

// Your task is to implement the function reverseStringRetainCase so that the program runs successfully.

// IMPORTANT: Do not implement the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// Chennai TamilNadu

// Output:
// Iannehc UdanlImat

// Explanation:
// Here the given string is Chennai TamilNadu.
// After reversing each word based on the given conditions, the string becomes Iannehc UdanlImat.

// Example Input/Output 2:
// Input:
// GoogleChrome FireFox MicrosoftEdge

// Output:
// EmorhcElgoog XofeRif EgdetfosoRcim










#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void reverseStringRetainCase(char *str)
{   
    char *ans = malloc(1000);
    char *token = strtok(str," ");
    int ind,i;
    while(token){
        ind = 0;
        for(i= strlen(token)-1;i>=0;i--){
            if(isupper(token[ind])){
                sprintf(ans,"%s%c",ans,toupper(token[i]));
            }else{
                sprintf(ans,"%s%c",ans,tolower(token[i]));
            }
            ind++;
        }
        sprintf(ans,"%s ",ans);
        token = strtok(NULL," ");
    }
    strcpy(str,ans);
}
int main()
{
    char str[1001];
    scanf("%[^\n]", str);
    reverseStringRetainCase(str);
    if(str[0] == '\0' || str[0] == ' ')
    {
        printf("String is empty\n");
    }
    printf("%s", str);
    return 0;
}