// Python - C - 005

// Please convert the following Python code to C so that the C program executes successfully passing the test cases.

// #Length of strVal is always less than or equal to 100
// strVal = input().strip()
// vowels = "aeiou"
// consonants = "BCDFGHJKLMNPQRSTVWXYZ"
// printed = False
// for ch in strVal:
//     if (not ch in vowels) and (not ch in consonants):
//         print(ch, end="")
//         printed = True
// if not printed:
//     print(-1)
 



// Max Execution Time Limit: 1000 millisecs






#include<stdio.h>
#include<stdlib.h>

int isVowel(char c){
    return (c=='a'||c=='e'||c=='i'||c=='o'||c=='u')?1:0;
}

int isConsonent(char c){
    return (c=='A'||c=='E'||c=='I'||c=='O'||c=='U')?0:1;
}

int main()
{
    char s[101];
    scanf("%s",s);
    int i=0,printed=0;
    while(s[i]!='\0'){
        if((islower(s[i]) && !isVowel(s[i])) || (isupper(s[i]) && !isConsonent(s[i]))){
            printf("%c",s[i]);
            printed=1;
        }
        i++;
    }
    if(!printed){
        printf("-1");
    }
}