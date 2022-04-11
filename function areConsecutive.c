// function areConsecutive
// The function/method areConsecutive accepts an argument str. The string str contains only digits.

// The function/method areConsecutive must return 1 if the given string represents the concatenation of two consecutive integers. Else the function must return 0.

// Your task is to implement the function areConsecutive so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 256257

// Output:
// 1

// Explanation:
// Here the given string is 256257.
// The two integers in the string are 256 and 257 which are consecutive.
// So 1 is printed as the output.

// Example Input/Output 2:
// Input:
// 4241

// Output:
// 1

// Example Input/Output 3:
// Input:
// 99100

// Output:
// 1

// Example Input/Output 4:
// Input:
// 20412024

// Output:
// 0







#include <stdio.h>
#include <stdlib.h>
int areConsecutive(char *str)
{
    int first,second;
    for(int i=0;str[i];i++)
    {
        char temp=str[i+1];
        str[i+1]='\0';
        first=atoi(str);
        str[i+1]=temp;
        second=atoi(str+i+1);
        if(str[i+1]=='0') continue;
    
        if(second-1==first||second+1==first) return 1;
    }
    return 0;
}
int main()
{
    char str[101];
    scanf("%s", str);
    printf("%d", areConsecutive(str));
    return 0;
}