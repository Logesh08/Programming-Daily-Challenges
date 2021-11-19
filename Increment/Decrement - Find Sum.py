# Increment/Decrement - Find Sum
# The program must accept N string values representing N integers as the input. Each integer may or may not have an increment operator or a decrement operator. The program must increment or decrement the values of the integers by 1 based on the operator. Finally, the program must print the sum of N resulting integers as the output.

# Boundary Condition(s):
# 1 <= N <= 100
# -10^6 <= Each integer value <= 10^6

# Input Format:
# The first line contains N.
# The second line contains N integers separated by a space.

# Output Format:
# The first line contains an integer representing the sum of the N resulting integer values.

# Example Input/Output 1:
# Input:
# 5
# 4++ 3 2-- 10++ 15

# Output:
# 35

# Explanation:
# 4++ => 5
# 2-- => 1
# 10++ => 11
# The revised integer values are 5, 3, 1, 11 and 15.
# The sum of the revised integer values is 35.

# Example Input/Output 2:
# Input:
# 4
# -5++ -6-- 5++ 7--

# Output:
# 1





def func(val):
    if '+' in val:
        return int(val[:-2])+1
    elif '-' in val[1:]:
        return int(val[:-2])-1
    else:
        return int(val)
(input())
print(sum(list(map(func,input().split() ))))