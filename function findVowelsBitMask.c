// function findVowelsBitMask
// The function/method findVowelsBitMask accepts an argument str representing a string value.

// The function/method findVowelsBitMask must return an integer value X whose binary representation indicates the presence of vowels in the given string by ignoring case. The 5 vowels (aeiou or AEIOU) are mapped to 5 bits in the binary representation of X starting from LSB(least significant bit). The presence of the vowels must be indicated by the set bits in the binary representation of X.

// Your task is to implement the function findVowelsBitMask so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// SkillRack

// Output:
// 5

// Explanation:
// There are two vowels 'i' and 'a' in the string "SkillRack".
// So the binary representation of X = 00101.
// The 1st bit from LSB indicates the presence of the vowel 'a'.
// The 3rd bit from LSB indicates the presence of the vowel 'i'.
// The decimal equivalent of 00101 is 5.

// Example Input/Output 2:
// Input:
// Archaeologist

// Output:
// 15

// Explanation:
// The binary representation of 15 is 01111.
// The last four bits indicate the presence of the vowels 'o', 'i', 'e' and 'a'.









#include <stdio.h>
#include <stdlib.h>
int findVowelsBitMask(char str[])
{
    int arr[5]={0};
    for(int i=0;i<strlen(str);i++)
    {
        if(tolower(str[i])=='a')
        arr[4]=1;
        else if(tolower(str[i])=='e')
        arr[3]=1;
        else if(tolower(str[i])=='i')
        arr[2]=1;
        else if(tolower(str[i])=='o')
        arr[1]=1;
        else if(tolower(str[i])=='u')
        arr[0]=1;
    }
   int sum=0,t=0;
    for(int i=5-1;i>=0;i--)
    {
        
      sum=sum+(arr[i]*pow(2,t));
      t++;
      //printf("%d",sum);
    }
    return sum;
}
int main()
{
    char str[101];
    scanf("%s", str);
    printf("%d", findVowelsBitMask(str));
    return 0;
}