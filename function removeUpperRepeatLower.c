// function removeUpperRepeatLower
// The function/method removeUpperRepeatLower accepts an argument str representing a string value.

// The function/method removeUpperRepeatLower must form a new string based on the following conditions.
// - Whenever an upper case alphabet occurs, repeat(duplicate) the previous alphabet once and then remove the upper case alphabet. If there is no previous alphabet for an upper case alphabet, then the function must remove that upper case alphabet.
// - Whenever a lower case alphabet occurs, keep the alphabet as it is.
// Then the function must return the new string. If all the alphabets in the string str are upper case, then the new string will be empty and hence the function must return "-1" as a string value.

// Your task is to implement the function removeUpperRepeatLower so that the program runs successfully.

// IMPORTANT: Do not implement the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// GreenApple

// Output:
// reennpple

// Explanation:
// Here S = "GreenApple".
// 1st alphabet G: Upper case alphabet. There is no previous alphabet. So G is removed.
// New string will be empty.

// 2nd, 3rd, 4th and 5th alphabets are lower case. They are kept as such.
// New string becomes "reen".

// 6th alphabet A: Upper case alphabet. The previous alphabet is n. So n is repeated.
// New string becomes "reenn".

// 7th, 8th, 9th and 10th alphabets are lower case. They are kept as such.
// New string becomes "reennpple".

// Hence the output is
// reennpple

// Example Input/Output 2:
// Input:
// SKILLRACK

// Output:
// -1

// Example Input/Output 3:
// Input:
// aBcDeFGH

// Output:
// aacceeee



#include <stdio.h>
#include <stdlib.h>

char* removeUpperRepeatLower(char *str)
{
    char *ptr = malloc(sizeof(char)*strlen(str));
    int index=0,i=0,yes=0;
    while(str[i]!='\0'){
        if(islower(str[i])){
            ptr[index++]=str[i];
            yes=1;
        } 
        else if(yes) ptr[index++]=ptr[index-1];
        i++;
    }
    if(yes==0){
        ptr="-1";
    }else{
        ptr[index]='\0';
    }
    return ptr;
}

int main()
{
    char str[1001];
    scanf("%s", str);
    char *newStr = removeUpperRepeatLower(str);
    if(str == newStr)
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