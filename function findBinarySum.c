// function findBinarySum
// The function/method findBinarySum accepts two arguments N and binValues. The binValues represents a 2-D array of characters denoting the N binary string values.

// The function/method findBinarySum must return a string containing the binary sum of the given N binary string values.

// Your task is to implement the function findBinarySum so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Boundary Condition(s):
// 2 <= N <= 100
// 1 <= Length of each string <= 100

// Example Input/Output 1:
// Input:
// 2
// 10001
// 11001

// Output:
// 101010

// Explanation:
// Here N=2 and the given 2 binary string values are 10001 and 11001.
// The sum of two binary string values 10001 and 11001 is 101010.

// Example Input/Output 2:
// Input:
// 3
// 1000
// 111
// 100010

// Output:
// 110001









#include <stdio.h>
#include <stdlib.h>
#include<math.h>
#include<string.h>
char * twonumbers(char *a, char *b)
{
    char arr[101];
    int len1 = strlen(a)-1,len2 = strlen(b)-1;
    int sum=0,ind=0,iter=0;
    while(len1>=0 || len2>=0 || sum == 1)
    {
        if(len1>=0)
        {
            sum += a[len1] - '0';
        }
        if(len2>=0)
        {
            sum += b[len2] - '0';
        }
        ind+=sprintf(arr+ind,"%d",(sum%2));
        sum = sum / 2;
        len1--;
        len2--;
    }
    
    char *fin = (char *)malloc(sizeof(char)*101);
    for(int index=strlen(arr)-1; index>=0; index--)
    {
        fin[iter++] = arr[index]; 
    }
    return fin;
}
char* findBinarySum(int N, char binValues[N][101])
{
    char *result = malloc(sizeof(char)*101);
    for(int index = 0; index<N; index++)
    {
        strcpy(result,twonumbers(result,binValues[index]));
    }
    return result;
}    
int main()
{
    int N;
    scanf("%d", &N);
    char str[N][101];
    for(int index = 0; index < N; index++)
    {
        scanf("%s", str[index]);
    }
    char *binarySum = findBinarySum(N, str);
    if(binarySum == NULL || binarySum == str[0])
    {
        printf("String is not formed\n");
    }
    if(binarySum[0] == '\0' || binarySum[0] == ' ')
    {
        printf("String is empty\n");
    }
    printf("%s", binarySum);
    return 0;
}