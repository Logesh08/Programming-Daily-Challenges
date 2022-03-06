# Smallest 5-Digit Integer
# The program must accept an integer S as the input. The program must print the smallest 5-digit integer whose sum of digits is equal to S. If it is not possible to form such an integer, then the program must print -1 as the output.

# Boundary Condition(s):
# 1 <= S <= 50

# Input Format:
# The first line contains S.

# Output Format:
# The first line contains the smallest 5-digit integer whose sum of digits is equal to S.

# Example Input/Output 1:
# Input:
# 10

# Output:
# 10009

# Explanation:
# Here S = 10.
# The smallest possible 5-digit integer that can be formed is 10009 (1 + 0 + 0 + 0 + 9 = 10).

# Example Input/Output 2:
# Input:
# 46

# Output:
# -1

# Example Input/Output 3:
# Input:
# 25

# Output:
# 10699






def findSmallest(m,s):
    if (s == 0):
         
        if(m == 1) :
              print("0")
        else :
              print("-1")
        return
  
    if (s > 9*m):
     
        print("-1")
        return
    res=[0 for i in range(m+1)]
    s -= 1
  
    for i in range(m-1,0,-1):
        if (s > 9):
         
            res[i] = 9
            s -= 9
     
        else:
         
            res[i] = s
            s = 0
    res[0] = s + 1
    for i in range(m):
        print(res[i],end="")
 
 
s = int(input())
findSmallest(5, s)
 