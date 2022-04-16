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
char* findBinarySum(int N, char binValues[N][101])
{
    int i = 0,len;
    long long int sum=0;
    for(;i<N;i++){
        len = strlen(binValues[i]);
        int itr=0,rem;
        long long int d=0;
        for(int x=len-1;x>=0;x--){
            rem = binValues[i][x] - 48;
            d += rem * pow(2,itr);
            itr++;
        }
        if(len>10) printf("%lld\n",d);
        sum += d;
    }
    
    char *answer = malloc(999999);
    char tmp [999];
    int n=sum;
    for(i=0;n>0;i++){
        tmp[i] = n%2;
        n/=2;
    }
    int d=0;
    n=i;
    for(i=n-1;i>=0;i--){
        sprintf(answer,"%s%d",answer,tmp[i]);
    }
    return answer;
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