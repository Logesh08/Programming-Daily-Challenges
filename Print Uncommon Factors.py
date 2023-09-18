# Print Uncommon Factors

# The program must accept two integers X and Y as the input. The program must print the uncommon factors of X and Y in descending order as the output. If there is no uncommon factor then the program must print -1 as the output.

# Boundary Condition(s):
# 1 <= X, Y <= 1000

# Input Format:
# The first line contains X and Y separated by a space.

# Output Format:
# The first line contains either the uncommon factors of X and Y or -1.

# Example Input/Output 1:
# Input:
# 24 100

# Output:
# 100 50 25 24 20 12 10 8 6 5 3

# Explanation:
# The factors of 24 are 1, 2, 3, 4, 6, 8, 12 and 24.
# The factors of 100 are 1, 2, 4, 5, 10, 20, 25, 50 and 100.
# Here the uncommon factors are 3, 5, 6, 8, 10, 12, 20, 24, 25, 50 and 100. So they are printed in descending order as the output.

# Example Input/Output 2:
# Input:
# 36 36

# Output:
# -1





x,y = map(int,input().split())
a = []
b = []
all = []
X=x;Y=y
while X > 1:
    if x%X==0:
        a.append(X)
        all.append(X)
    X-=1
while Y > 1:
    if y%Y==0:
        b.append(Y)
        if Y not in all:
            all.append(Y)
    Y-=1
notPrinted = True
for i in sorted(all)[::-1]:
    if (i in a and i not in b) or (i in b and i not in a):
        print(i,end=' ')
        notPrinted=False
if notPrinted:
    print(-1)