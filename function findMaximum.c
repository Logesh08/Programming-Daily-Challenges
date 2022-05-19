// function findMaximum
// The function/method findMaximum accepts four arguments R, C, matrix and K. The first two arguments R and C represent the size of an integer matrix. The third argument represents the R*C integer matrix. The fourth argument represents an integer value.

// The function/method findMaximum must form an integer matrix of size M*N, where M = R/K and N = C/K. Then the function must fill the matrix with the maximum value in each K*K submatrix of the given matrix. Finally, the function must return the M*N matrix.

// Note: The values of R and C are always divisible by K.

// Your task is to implement the function findMaximum so that it passes all the test cases.

// The following structure is used to represent the boundedArray and is already defined in the default code (Do not write this definition again in your code).
// typedef struct BoundedArray
// {
//     int M, N;
//     int **matrix;
// } boundedArray;

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 9 9
// 18 38 31 65 47 68 96 49 31
// 30 23 83 78 38 19 24 94 43
// 24 17 49 21 94 84 86 53 78
// 43 67 64 42 68 13 95 85 64
// 27 54 69 76 43 37 92 19 26
// 61 58 84 85 83 36 11 17 15
// 20 24 50 74 58 17 40 20 90
// 82 31 24 88 78 68 67 24 72
// 69 24 87 41 32 68 37 79 80
// 3

// Output:
// 83 94 96
// 84 85 95
// 87 88 90

// Explanation:
// Here R = 9, C = 9 and K = 3.
// So the maximum value in each 3*3 submatrix is printed as the output.

// Example Input/Output 2:
// Input:
// 6 8
// 26 13 27 55 35 51 78 24
// 72 83 25 80 34 10 60 17
// 14 36 38 77 67 47 41 15
// 61 69 42 82 63 86 43 56
// 66 22 19 53 87 12 57 50
// 81 49 46 44 23 90 62 11
// 2

// Output:
// 83 80 51 78
// 69 82 86 56
// 81 53 90 62









#include <stdio.h>
#include <stdlib.h>

typedef struct BoundedArray
{
    int M, N;
    int **matrix;
} boundedArray;
boundedArray* findMaximum(int R, int C, int *matrix, int K)
{
    boundedArray *ba = malloc(sizeof(boundedArray));
    ba->M=R/K;
    ba->N=C/K;
    ba->matrix=malloc(sizeof(int*)*R);
    for(int i=0;i<ba->M;i++)
    {
        ba->matrix[i]=malloc(sizeof(int)*C);
        for(int j=0;j<ba->N;j++)
        {
            int max=0;
            for(int ii=i*K;ii<i*K+K;ii++)
            {
                for(int jj=j*K;jj<j*K+K;jj++)
                {
                    max=matrix[ii*C+jj]>max?matrix[ii*C+jj]:max;
                }
            }
            ba->matrix[i][j]=max;
        }
    }
    return ba;

} // End of findMaximum function
int main()
{
    int R, C, K;
    scanf("%d %d", &R, &C);
    int matrix[R][C];
    for(int row = 0; row < R; row++)
    {
        for(int col = 0; col < C; col++)
        {
            scanf("%d", &matrix[row][col]);
        }
    }
    scanf("%d", &K);
    boundedArray *bArr = findMaximum(R, C, matrix, K);
    if(bArr == NULL)
    {
        printf("Matrix is not formed\n");
    }
    if(bArr->M <= 0 || bArr->N <= 0)
    {
        printf("Invalid size for the matrix\n");
    }
    for(int row = 0; row < bArr->M; row++)
    {
        for(int col = 0; col < bArr->N; col++)
        {
            printf("%d ", bArr->matrix[row][col]);
        }
        printf("\n");
    }
    return 0;
} // End of main() function