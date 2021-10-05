# Stretched String
# The program must accept two string values S1 and S2. If S2 is a stretched string of S1, the program must print Yes. Else the program must print No. A stretch is to repeat each character in a string the same number of times. Also no additional characters must be present is S2.

# Boundary Condition(s):
# 1 <= Length of S1, S2 <= 1000

# Input Format:
# The first line contains S1.
# The second line contains S2.

# Output Format:
# The first line contains Yes or No.

# Example Input/Output 1:
# Input:
# cake
# cccaaakkkeee

# Output:
# Yes

# Explanation:
# Here each character in S2 is repeated 3 times and no additional characters. Hence S2 is a stretched version of S1.

# Example Input/Output 2:
# Input:
# cake
# ccaaaakkkeee

# Output:
# No

# Example Input/Output 3:
# Input:
# cake
# ccaakkeess

# Output:
# No

# Explanation:
# Here s is an additional character. Hence S2 is not a stretched version of S1.

# Example Input/Output 4:
# Input:
# eel
# eeeeeelll

# Output:
# Yes




a=input().strip()
b=input().strip()
new=""
mul=len(b)//len(a)
if len(b)%len(a)!=0:
    print("No")
else:
    for c in a:
        new+=c*mul
    if new==b:
        print("Yes")
    else:
        print("No")
