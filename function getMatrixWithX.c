// function getMatrixWithX
// The function/method getMatrixWithX accepts three arguments R, C and X. The integers R and C represent the size of the integer matrix to be formed. The integer X represents the value to be filled in the matrix.

// The function/method getMatrixWithX must form an integer matrix of size R*C. Then the function must initialize each integer with X in the matrix. Finally, the function must return the matrix.

// Your task is to implement the function getMatrixWithX so that it passes all the test cases.

// The following structure is used to represent the boundedArray and is already defined in the default code (Do not write this definition again in your code).
// typedef struct BoundedArray
// {
//     int R, C;
//     int **matrix;
// } boundedArray;

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 4 5 10

// Output:
// 10 10 10 10 10
// 10 10 10 10 10
// 10 10 10 10 10
// 10 10 10 10 10

// Explanation:
// Here R=4, C=5 and X=10.
// So the integer matrix is formed with the size 4*5 then the matrix is filled with the integer value 10.
// Hence the output is
// 10 10 10 10 10
// 10 10 10 10 10
// 10 10 10 10 10
// 10 10 10 10 10

// Example Input/Output 2:
// Input:
// 5 3 -50

// Output:
// -50 -50 -50
// -50 -50 -50
// -50 -50 -50
// -50 -50 -50
// -50 -50 -50











#include <stdio.h>
#include <stdlib.h>

typedef struct BoundedArray
{
    int R, C;
    int **matrix;
} boundedArray;
  
boundedArray* getMatrixWithX(int R, int C, int X)
{
    boundedArray *barr = malloc(90001);
    barr->matrix = (int**)malloc(R*sizeof(int*));
    for(int i=0;i<R;i++){
        barr->matrix[i]=malloc(sizeof(int)*C);
        for(int j=0;j<C;j++)
            barr->matrix[i][j]=X;
        
    }
    barr->C=C;
    barr->R=R;
    return barr;
    
}


int main()
{
    int R, C, X;
    scanf("%d %d %d", &R, &C, &X);
    boundedArray *bArr = getMatrixWithX(R, C, X);
    if(bArr == NULL || bArr->matrix == NULL || bArr->R != R || bArr->C != C)
    {
        printf("Matrix is not formed properly\n");
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
}
