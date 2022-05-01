# Rook Game
# Two players A and B are playing a game. In that game, there is a chessboard of size R*C, where they take turns placing the rooks. The cells with the rook are represented by 1. The empty cells are represented by 0. In each turn, a player must place a rook.

# A rook may be placed on the basis of the following conditions.
# - The cell must be an empty cell.
# - There should be no rook in the row and column of the cell.

# When a player is unable to make a move, he loses and the game ends. The initial state of the chessboard is passed as the input to the program. The program must print the winner of the game if player A starts the game.
# Note: Both the players have an infinite number of rooks to play the game.

# Boundary Condition(s):
# 2 <= R, C <= 50

# Input Format:
# The first line contains R and C separated by a space.
# The next R lines, each contains C integers separated by a space.

# Output Format:
# The first line contains A or B.

# Example Input/Output 1:
# Input:
# 3 3
# 1 0 0
# 0 0 0
# 1 0 0

# Output:
# A

# Explanation:
# If player A puts the rook in the cell (2, 3) or (2, 2), player B will have no moves.
# So A wins the game.

# Example Input/Output 2:
# Input:
# 3 2
# 1 1
# 0 1
# 1 0

# Output:
# B

# Explanation:
# Here player A cannot make a move, so B wins the game.

# Example Input/Output 3:
# Input:
# 2 2
# 0 0
# 0 0

# Output:
# B

# Explanation:
# The one possible way is given below.
# Player A puts the rook in the cell (1, 1). Then player B puts the rook in the cell (2, 2).
# Now the player A cannot make a move, so B wins the game.














r,c = map(int,input().split())
mat = [input().split() for _ in range(r)]
count = 0
while True:
    for i in range(r):
        for j in range(c):
            if '1' not in mat[i] and '1' not in list(zip(*mat))[j]:
                mat[i][j] = '1'
                count += 1
                continue 
    break
print('A' if count%2 else 'B')