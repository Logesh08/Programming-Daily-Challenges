# Calculator With Shift

# An expression consisting of two integers X and Y (as operands) and a character ch (as operator) is passed as input. Another integer shift is also passed as input to the program based on which the operations are shifted. If the shift value is 1 then the operations are shifted as per the conditions given below.

# Conditions:
# + must be considered as -
# - must be considered as +
# * must be considered as /
# / must be considered as *

# If the shift value is 0 then the given expression is evaluated without any modification. The program must evaluate the expression as per the conditions and print the result as the output.

# Note:
# Decimal place values are not considered when dividing.
# The allowed operators are +, -, * and /.

# Boundary Condition(s):
# -10000 <= X, Y <= 10000
# shift value is either 0 or 1.

# Input Format:
# The first line contains the value of X, ch and Y without any space.
# The second line contains the value of shift.

# Output Format:
# The first line contains the result of the expression.

# Example Input/Output 1:
# Input:
# 2+4
# 0

# Output:
# 6

# Example Input/Output 2:
# Input:
# 7*2
# 1

# Output:
# 3






s = input().strip()
if input().strip()=="0":
    print(eval(s.replace('/','//')))
else:
    print(eval(s.replace('*','m').replace('/','d').replace('-','s').replace('+','a').replace('m','//').replace('d','*').replace('s','+').replace('a','-')))