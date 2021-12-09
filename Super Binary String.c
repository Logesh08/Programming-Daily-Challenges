// Super Binary String
// The program must accept a string S containing only 0s and 1s as the input. The program must print Yes if the given string is a super binary string. Else the program must print No as the output. A super binary string must satisfy the following two conditions.
// - The number of 1s must be equal to the number of 0s.
// - In each prefix of the string, the number of 1s must be greater than or equal to the number of 0s in the prefix.

// Hint: Optimize your logic to avoid Time Limit Exceeded Error.

// Boundary Condition(s):
// 1 <= Length of S <= 10^6

// Input Format:
// The first line contains S.

// Output Format:
// The first line contains Yes or No.

// Example Input/Output 1:
// Input:
// 110010

// Output:
// Yes

// Explanation:
// Here S = "110010".
// The number of 1s in S = 3.
// The number of 0s in S = 3.
// In each prefix of S, the number of 1s is greater than or equal to the number of 0s.
// 1st prefix: 1
// 2nd prefix: 11
// 3rd prefix: 110
// 4th prefix: 1100
// 5th prefix: 11001
// 6th prefix: 110010
// Hence Yes is printed as the output.

// Example Input/Output 2:
// Input:
// 1001

// Output:
// No

// Example Input/Output 3:
// Input:
// 11010

// Output:
// No










#include<stdio.h>
#include<stdlib.h>

int main()
{
    char s[1000001];
    scanf("%s",s);
    int i=0, len = strlen(s),z=0,o=0;
    for(;i<len;i++){
        if (s[i]=='1') o++;
        else z++;
        if (z>o) {
            printf("No");
            return 0;
        }
    }
    printf(z==o?"Yes":"No");
}