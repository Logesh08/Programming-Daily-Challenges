# Convert 0's to 1's at Even Position(s)

# An integer N is passed as the input. The program must change all the bits present at even position(from last bit) to 1 and then print the modified decimal value as the output. 

# Boundary Condition(s):
# 2 <= N <= 500

# Input Format:
# The first line contains the value of N.

# Output Format:
# The first line contains modified decimal value.

# Example Input/Output 1:
# Input:
# 5

# Output:
# 7

# Explanation:
# The binary value of 5 is 101.
# Changing the bits at even position we get 111 = 7.

# Example Input/Output 2:
# Input:
# 32

# Output:
# 42

# Explanation:
# The binary value of 32 is 100000.
# Changing the bits at even position we get 101010 = 42.





(lambda x: print(int(''.join(['1' if i%2 else x[i] for i in range(len(x))])[::-1],2)))(bin(int(input()))[:1:-1])