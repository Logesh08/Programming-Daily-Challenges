# Fold String - Up or Down
# The program must accept a string S, a character CH and an integer X as the input. The program must fold the string up or down starting from the Xth character. The character CH denotes the folding type (u or U for up, d or D for down). The program must print the folded string as the output. The empty spaces must be printed as asterisks.

# Boundary Condition(s):
# 2 <= Length of S <= 1000
# 2 <= X <= Length of S

# Input Format:
# The first line contains S.
# The second line contains CH and X separated by a space.

# Output Format:
# The first two lines contain the folded string based on the given conditions.

# Example Input/Output 1:
# Input:
# SkillRack
# U 6

# Output:
# *kcaR
# Skill

# Explanation:
# Here S = "SkillRack", CH = 'U' and X = 6.
# So the string S is folded up from the 6th character.
# Hence the output is
# *kcaR
# Skill

# Example Input/Output 2:
# Input:
# SkillRack
# d 3

# Output:
# *****Sk
# kcaRlli

# Example Input/Output 3:
# Input:
# notebook
# u 5

# Output:
# koob
# note





a=input().strip()
c,b=map(str,input().split())
b=int(b)-1
if(c=='U' or c=='u'):
    d,e=a[b:][::-1],a[:b]
if(c=='d' or c=='D'):
    d,e=a[:b],a[b:][::-1]
d,e=list(d),list(e)
if(len(d)<len(e)):
    for i in range(abs(len(d)-len(e))):
        d.insert(0,'*')
if(len(e)<len(d)):
    for i in range(abs(len(d)-len(e))):
        e.insert(0,'*')
d="".join(d)
e="".join(e)
print(d)
print(e)