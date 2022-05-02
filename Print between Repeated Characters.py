# Print between Repeated Characters
# The program must accept a string S as the input. The program must print the characters between the repeated characters(inclusive) as the output. If there are no repeating characters, then the program must print -1 as the output.

# Boundary Condition(s):
# 2 <= Length of S <= 1000

# Input Format:
# The first line contains S.

# Output Format:
# The lines contain the characters between the repeated characters(inclusive) or -1 as the output.

# Example Input/Output 1:
# Input:
# skillrack

# Output:
# killrack
# ll

# Explanation:
# The string skillrack has two repeated characters k and l.
# killrack -> The characters between the two occurrences of k are printed as the output.
# ll -> The characters between the two occurrences of l are printed as the output.

# Example Input/Output 2:
# Input:
# qualification

# Output:
# alifica
# ifi
# icati

# Example Input/Output 3:
# Input:
# svghakjufr

# Output:
# -1

# Example Input/Output 4:
# Input:
# bbaabbaabb

# Output:
# bb
# baab
# bb
# baab
# bb
# aa
# abba
# aa













s = list(input().strip())
uniq = sorted(set(s),key = lambda x: s.index(x))
notPrinted = True
for i in uniq:
    t = s.copy()
    cur = t.index(i)
    t[cur] = '*'
    while i in t:
        end = t.index(i)
        print(''.join(s[cur:end+1]))
        notPrinted = False
        t[end] = '*'
        cur = end
if notPrinted:
    print(-1)