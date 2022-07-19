# Check if the Chessboard is Valid or Invalid

# A chessboard of size N*N is given as the input to the program. B represents black colored squares and W represents white colored squares. A chessboard is valid only if it has alternate black and white squares both vertically and horizontally. The program must print Valid if the chessboard is valid. Else the program must print Invalid.

# Boundary Condition(s):
# 2 <= N <= 20

# Input Format:
# The first line contains the value of N.
# The next N lines contain the characters either W or B.

# Output Format:
# The first line contains the either valid or invalid.

# Example Input/Output 1:
# Input:
# 4
# WBWB
# BWBW
# WBWB
# BWBW

# Output:
# Valid

# Example Input/Output 2:
# Input:
# 4
# WBWB
# BWBW
# WBWB
# BWBB

# Output:
# Invalid








n = int(input())
board = [input().strip() for _ in range(n)]
def get(c):
    if c=='W': return 'B'
    else: return 'W'
for i in range(1,n-1):
    for j in range(1,n-1):
        if board[i][j] in [board[i][j+1],board[i][j-1],board[i+1][j],board[i-1][j]] or get(board[i][j]) in [board[i+1][j+1],board[i-1][j+1],board[i-1][j-1],board[i+1][j-1]]:
            print("Invalid")
            exit()
print("Valid")