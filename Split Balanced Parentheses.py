# Split Balanced Parentheses
# The program must accept a string S as the input. The string S contains only parentheses, where each open parenthesis '(' has a matching close parenthesis ')'. The program must split the string S into as many substrings as possible, where the parentheses in each substring must be balanced.

# Boundary Condition(s):
# 2 <= Length of S <= 100

# Input Format:
# The first line contains S.

# Output Format:
# The lines contain the substrings of S based on the given conditions.

# Example Input/Output 1:
# Input:
# ()()

# Output:
# ()
# ()

# Explanation:
# There are two balanced substrings in S.
# Hence the output is
# ()
# ()

# Example Input/Output 2:
# Input:
# ()((())())((()))(()(())())

# Output:
# ()
# ((())())
# ((()))
# (()(())())

# Example Input/Output 3:
# Input:
# (()(()()))()(((()))()(()))(()((()))(())())(())()

# Output:
# (()(()()))
# ()
# (((()))()(()))
# (()((()))(())())
# (())
# ()




string=input().strip()
pairsCount=0
i=0
while i<len(string):
    c=string[i]
    if c=='(':
        pairsCount+=1 
    elif c==')':
        pairsCount-=1
    if pairsCount==0:
        string=string[:i+1]+'\n'+string[i+1:]
        i+=1
    i+=1
print(string.strip())
