# Kth Integer in Odd Even Sequence

# The program must accept two integers N and K as the input. The program must generate a sequence of integers containing all the odd integers from 1 to N followed by all the even integers from 1 to N. Then the program must print the Kth integer in sequence as the output.

# Boundary Condition(s):
# 1 <= K <= N <= 10^5

# Input Format:
# The first line contains N and K separated by a space.

# Output Format:
# The first line contains the Kth integer in sequence.

# Example Input/Output 1:
# Input:
# 10 3

# Output:
# 5

# Explanation:
# Here N = 10, so the sequence is 1 3 5 7 9 2 4 6 8 10.
# The third integer in the sequence is 5, so it is printed as the output.

# Example Input/Output 2:
# Input:
# 7 7

# Output:
# 6




N,K=map(int,input().split())

if K <= (N + 1) // 2:
    result = 2 * K - 1
else:
    K -= (N + 1) // 2
    result = 2 * K
print(result)