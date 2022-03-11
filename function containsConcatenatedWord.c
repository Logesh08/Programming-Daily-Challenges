// function containsConcatenatedWord
// The function/method containsConcatenatedWord accepts an argument str. The string str contains multiple words separated by a space.

// The function/method containsConcatenatedWord must return 1 if the given str contains a word which is equal to the concatenation of any two words in any order. Else the function must return 0.

// Your task is to implement the function containsConcatenatedWord so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// rat lion cat ratcat tiger

// Output:
// 1

// Explanation:
// rat + cat = ratcat, which is equal to the 4th word in the given string.
// Hence 1 is printed.

// Example Input/Output 2:
// Input:
// rat lion cat ratcatpig tiger

// Output:
// 0

// Example Input/Output 3:
// Input:
// zebra fox monkey donkey wolf donkeyfox

// Output:
// 1








#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>

#include<string.h>
int containsConcatenatedWord(char *str)
{
    char words[999][999];
    char *token = strtok(str," ");
    int i=0,n=0;
    while(token!=NULL){
        strcpy(words[n++],token);
        token = strtok(NULL," ");
    }
   for(;i<n;i++){
       for(int j=0;j<n;j++){
       char temp[999999];
            strcpy(temp,words[i]);
           strcat(temp,words[j]);
           for(int x=0;x<n;x++){
                if(strcmp(words[x],temp)==0) return 1;
               
           }
       }
   }
   return 0;
}



int main()
{
    char str[10001];
    scanf("%[^\n]", str);
    printf("%d", containsConcatenatedWord(str));
    return 0;
}