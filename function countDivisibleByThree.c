// function countDivisibleByThree
// The function/method countDivisibleByThree accepts an argument str representing a string value. The string str contains only digits and it represents an integer.

// The function/method countDivisibleByThree must return an integer denoting the number of integers divisible by 3 that can be obtained by changing at most one digit in the given string.

// Your task is to implement the function countDivisibleByThree so that the program runs successfully.

// IMPORTANT: Do not implement the main() function as it is already defined.

// Boundary Condition(s):
// 1 <= Length of the given string <= 100

// Example Input/Output 1:
// Input:
// 23

// Output:
// 7

// Explanation:
// The 7 possible ways are given below.
// 03, 21, 24, 27, 33, 63 and 93.

// Example Input/Output 2:
// Input:
// 100

// Output:
// 10

// Example Input/Output 3:
// Input:
// 28041587931619954605240353727

// Output:
// 69







#include <stdio.h>
#include <stdlib.h>

int countDivisibleByThree(char *str)
{
    int i=0,l=strlen(str),j,sum=0,cur,count=0;
    while(str[i]!='\0'){
        sum+= str[i] - '0';
        i++;
    }
    i=0;
    while(str[i]!='\0'){
        cur = (str[i] - '0');
        for(j = 0;j<10;j++){
            if(j!=cur && (sum - cur + j)%3==0){
                count++;
            }
        }
        i++;
    }
    return count;
}

int main()
{
    char str[101];
    scanf("%s", str);
    printf("%d", countDivisibleByThree(str));
    return 0;
}