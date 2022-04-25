// function findMaxCost
// A box is represented as:
// struct Box
// {
//     int pens;
//     int pencils;
//     int erasers;
// };
// The above structure is already defined in the default code (Do not write this definition again in your code).

// The function/method findMaxCost accepts two arguments N and boxes. The array 'boxes' represents an array of type 'Box' and it contains N elements. Each element of boxes consists of three positive integers 'pens', 'pencils' and 'erasers' representing the count of pens, pencils and erasers in a box respectively. The cost of a pen, pencil and eraser are 10, 5 and 3 respectively.

// The function/method findMaxCost must return an integer representing the maximum cost of a box among the given N boxes.

// Your task is to implement the function findMaxCost so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 4
// 2 5 1
// 1 2 3
// 3 1 3
// 3 3 3

// Output:
// 54

// Explanation:
// 1st box: 2 pens, 5 pencils and 1 eraser. Total cost = 48 (2*10 + 5*5 + 1*3).
// 2nd box: 1 pen, 2 pencils and 3 erasers. Total cost = 29 (1*10 + 2*5 + 3*3).
// 3rd box: 3 pens, 1 pencil and 3 erasers. Total cost = 44 (3*10 + 1*5 + 3*3).
// 4th box: 3 pens, 3 pencils and 3 erasers. Total cost = 54 (3*10 + 3*5 + 3*3).
// The 4th box having the maximum cost 54.
// So 54 is printed as the output.

// Example Input/Output 2:
// Input:
// 2
// 10 1 1
// 5 10 10

// Output:
// 130










#include <stdio.h>
#include <stdlib.h>

struct Box
{
    int pens;
    int pencils;
    int erasers;
};


int findMaxCost(int N, struct Box boxes[])
{
    int max=0,t,i; 
    for(i=0;i<N;i++){ 
        t = (10*boxes[i].pens) + (5*boxes[i].pencils)+(3*boxes[i].erasers); 
        if(t>max) max = t;
    }
    return max;
}

int main()
{
    int N;
    scanf("%d", &N);
    struct Box boxes[N];
    for(int index = 0; index < N; index++)
    {
        scanf("%d %d %d", &boxes[index].pens, &boxes[index].pencils, &boxes[index].erasers);
    }
    printf("%d", findMaxCost(N, boxes));
    return 0;
}