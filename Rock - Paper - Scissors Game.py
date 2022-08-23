# Rock - Paper - Scissors Game

# Two players are playing Rock - Paper - Scissors game. The program must accept an integer N (number of rounds) as the input. The winner in each round is decided based on the following priority. Rock has more priority than scissors, scissors has more priority than paper and paper has more priority than rock. The program must print the player who wins the match as the output. If no one wins the match, then "Tie" is printed as the output.

# Boundary Condition(s):
# 1 <= N <= 50

# Input Format:
# The first line contains the value of N.
# The next N lines contain the choice of the two players each separated by space.

# Output Format:
# The first line contains either Tie or name of the player who wins the match.

# Example Input/Output 1:
# Input:
# 5
# rock rock 
# paper rock 
# scissors paper 
# scissors rock
# paper paper

# Output:
# 1

# Explanation:
# At the end of 1st round, no one won the game.
# At the end of 2nd round, the 1st player won the game.
# At the end of 3rd round, the 1st player won the game.
# At the end of 4th round, the 2nd player won the game.
# At the end of 5th round, no one won the game.
# At the end of all rounds, the 1st player won more matches than the 2nd player.
# So, 1 is printed as output.

# Example Input/Output 2:
# Input:
# 3
# paper scissors
# paper paper
# scissors scissors

# Output:
# 2

# Example Input/Output 3:
# Input:
# 4
# rock scissors
# scissors rock
# paper rock
# rock paper

# Output:
# Tie










a=b=0
n = int(input())
for _ in range(n):
    x,y = map(lambda x:x[0],input().split())
    if x!=y:
        if x=='r':
            if y=='p': b+=1
            else: a+=1
        elif x=='p':
            if y=='r': a+=1
            else: b+=1 
        else:
            if y=='r': b+=1 
            else: a+=1 
print(1 if a>b else 2 if b>a else 'Tie')