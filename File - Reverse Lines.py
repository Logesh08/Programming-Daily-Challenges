# File - Reverse Lines
# The program must accept a string S denoting the name of a text file and an integer N as the input. The program must read the first N lines from the given file. Then the program must print the N lines in reverse order as the output.

# Note: The given file is always present in the same folder where the program executes.

# Boundary Condition(s):
# 5 <= Length of S <= 20
# 1 <= N <= Number of lines in the file <= 100
# 1 <= Length of each line in the file <= 100

# Input Format:
# The first line contains S.
# The second line contains N.

# Output Format:
# The first N lines contain the first N lines of the given file in reverse order.

# Example Input/Output 1:
# Input:
# input1.txt
# 5

# Output:
# rose
# red
# the
# pluck
# You

# Explanation:
# Here N = 5 and the input1.txt file is present in the same folder where the program executes and the file contains the following values.
# You
# pluck
# the
# red
# rose
# and
# go
# home

# So the first 5 lines in the file are printed in reverse order.

# Example Input/Output 2:
# Input:
# input2.txt
# 2

# Output:
# Dog
# Lion

# Explanation:
# Here N = 2 and the input2.txt file is present in the same folder where the program executes and the file contains the following values.
# Lion
# Dog
# Tiger
# Elephant
# Deer
# Horse

# So the first 2 lines in the file are printed in reverse order.









f = open(input().strip(),'r')
arr = f.read().split('\n')
for i in range(int(input())-1,-1,-1):
    print(arr[i])