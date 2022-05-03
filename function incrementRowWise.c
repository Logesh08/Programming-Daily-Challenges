// function incrementRowWise
// The function/method incrementRowWise accepts three arguments R, C and matrix. The integers R and C represent the size of the integer matrix.

// The function/method incrementRowWise must modify the given matrix by incrementing the value of each integer by its row position (i.e., Increment each integer in the 1st row by 1, increment each integer in the 2nd row by 2, increment each integer in the 3rd row by 3, and so on).

// Your task is to implement the function incrementRowWise so that the program runs successfully.

// IMPORTANT: Do not implement the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 3 3
// 1 2 3
// 4 5 6
// 7 8 9

// Output:
// 2 3 4
// 6 7 8
// 10 11 12

// Explanation:
// Here R = 3 and C = 3.
// 1st row: Each integer incremented by 1.
// 2nd row: Each integer incremented by 2.
// 3rd row: Each integer incremented by 3.

// Example Input/Output 2:
// Input:
// 4 5
// 10 20 30 40 50
// 8 18 28 38 48
// 55 44 33 22 11
// 6 7 8 9 10

// Output:
// 11 21 31 41 51
// 10 20 30 40 50
// 58 47 36 25 14
// 10 11 12 13 14







#include <stdio.h>
#include <stdlib.h>

void incrementRowWise(int R, int C, int *matrix)
{
    int i,j;
    for(i=0;i<R;i++){
        for(j=0;j<C;j++){
            matrix[(i*C)+j] += i+1;
        }
    }

} // End of incrementRowWise function

int main()
{
    int R, C;
    scanf("%d %d", &R, &C);
    int matrix[R][C];
    for(int row = 0; row < R; row++)
    {
        for(int col = 0; col < C; col++)
        {
            scanf("%d", &matrix[row][col]);
        }
    }
    incrementRowWise(R, C, matrix);
    for(int row = 0; row < R; row++)
    {
        for(int col = 0; col < C; col++)
        {
            printf("%d ", matrix[row][col]);
        }
        printf("\n");
    }
    return 0;
} // End of main() function


