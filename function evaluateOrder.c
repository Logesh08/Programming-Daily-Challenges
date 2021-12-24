// function evaluateOrder
// The function/method evaluateOrder accepts an argument str. The string str contains integers separated by the relational operators (greater than > and less than <).

// The function/method evaluateOrder must return the integer value 1 if all the relationships between the integers in the string are true. Else the function must return the integer value 0.

// Your task is to implement the function evaluateOrder so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Boundary Condition(s):
// 1 <= Each integer value in the given string <= 10^6

// Example Input/Output 1:
// Input:
// 10<20<50>10<400>5<6

// Output:
// 1

// Explanation:
// 10<20 = True
// 20<50 = True
// 50>10 = True
// 10<400 = True
// 400>5 = True
// 5<6 = True
// All the relationships between the integers are True.
// Hence 1 is printed as the output.

// Example Input/Output 2:
// Input:
// 450>255<300>301>101<102<555

// Output:
// 0

// Explanation:
// 450>255 = True
// 255<300 = True
// 300>301 = False
// 301>101 = True
// 101<102 = True
// 102<555 = True
// The 3rd relational operator returns False.
// Hence 0 is printed as the output.
 






 #include <stdio.h>
#include <stdlib.h>
int evaluateOrder(char *str)
{
   int nums[1001], x = 0, l = strlen(str), y = 0, z = 0;
   char curr_str[20], symbols[100];
   for(int i = 0; i <= l; i++)
   {
       if(str[i] == '<' || str[i] == '>' || str[i] == '\0')
       {
           curr_str[x] = '\0';
           x = 0;
           nums[y++] = atoi(curr_str);
           if(str[i] != '\0')
           {
               symbols[z++] = str[i];
           }
       }
       else
       {
           curr_str[x++] = str[i];
       }
   }
   x = 0;
   for(int i = 0; i < y-1; i++)
   {
       if(symbols[x] == '>')
       {
           if(nums[i] <= nums[i+1])
           {
               return 0;
           }
       }
       else
       {
           if(nums[i] >= nums[i+1])
           {
               return 0;
           }
       }
       x++;
   }
   return 1;
}
int main()
{
    char str[101];
    scanf("%s", str);
    printf("%d", evaluateOrder(str));
    return 0;
}