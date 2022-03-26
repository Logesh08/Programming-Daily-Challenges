// function removeRowsWithSameValue
// The function/method removeRowsWithSameValue accepts three arguments - R, C and matrix. The first two arguments R and C represent the size of an integer matrix. The third argument matrix represents a pointer to the integer matrix.

// The function/method removeRowsWithSameValue must remove the rows having the same value. Then the function must return the revised matrix. If all the rows of the matrix are removed, then the function must return a matrix of size 1*1 with the value -1.

// Your task is to fill in the missing lines of code to implement the function removeRowsWithSameValue so that it passes all the test cases.

// The following structure is used to represent the boundedArray and is already defined in the default code (Do not write this definition again in your code).
 
// typedef struct BoundedArray
// {
//     int R, C;
//     int **matrix;
// } boundedArray;

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 5 4
// 10 20 30 10
// 50 50 50 50
// 55 55 66 55
// 40 30 20 10
// 55 55 55 55

// Output:
// 10 20 30 10
// 55 55 66 55
// 40 30 20 10

// Explanation:
// All the values in the 2nd row are same.
// All the values in the 5th row are same.
// So the 2nd and 5th rows of the matrix are removed.

// Example Input/Output 2:
// Input:
// 3 3
// 4 4 4
// 8 8 8
// 2 2 2

// Output:
// -1








#include <stdio.h>
#include <stdlib.h>

typedef struct BoundedArray
{
    int R, C;
    int **matrix;
} boundedArray;

boundedArray* removeRowsWithSameValue(int R, int C, int *matrix)
{
    boundedArray* barr = malloc(99999);
    int i,j,row=0,col=0;
    barr->matrix = malloc(99999);
    for(i=0;i<R;i++){
        int same = 0;
        int cmp = matrix[(i*C)];
        for(j=1;j<C;j++){
            if(matrix[(i*C)+j]!=cmp){
                same=1;
                break;
            }
        }
        if(same){
            barr->matrix[row] = malloc(99999);
            for(j=0;j<C;j++){
                barr->matrix[row][j] = matrix[(i*C)+j];
            }
            row++;
        }
    }
    barr->R=row;
    barr->C=C;
    if(row==0){
        barr->matrix[0] = malloc(99999);
        barr->R=1;
        barr->C=1;
        barr->matrix[0][0] = -1;
    }
    return barr;
} // End of removeRowsWithSameValue function

int main()
{
    int R, C;
    scanf("%d %d", &R, &C);
    int matrix[R][C];
    for(int row = 0; row < R; row++)
    {
        for(int col = 0; col < C; col++)
        {
            scanf(" %d", &matrix[row][col]);
        }
    }
    boundedArray *bArr = removeRowsWithSameValue(R, C, matrix);
    if(bArr == NULL)
    {
        printf("Matrix is not formed\n");
    }
    if(bArr->R <= 0 || bArr->C <= 0)
    {
        printf("Invalid size for the revised matrix\n");
    }
    for(int row = 0; row < bArr->R; row++)
    {
        for(int col = 0; col < bArr->C; col++)
        {
            printf("%d ", bArr->matrix[row][col]);
        }
        printf("\n");
    }
    return 0;
} // End of main() function