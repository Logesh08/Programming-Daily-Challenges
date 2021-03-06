# Remove Unit Digits - Previous & Next
# The program must accept a list of N integers and an integer T as the input. The program must remove T unit digits in the given list of integers based on the following conditions.
# - The program must start removing the unit digits from the 1st integer.
# - If the removed unit digit is even, then the program must remove the unit digit of the next integer. Else the program must remove the unit digit of the previous integer.
# - Similarly, the program must remove T unit digits in the given list of integers.
# - Once all the digits in an integer are removed, then the integer itself must be removed from the given list.
# - Consider the given list of integers in circular fashion when finding the previous and next integers.
# Finally, the program must print the sum S of the modified integers in the list as the output. If all integers are removed, then the program must print -1 as the output.

# Boundary Condition(s):
# 2 <= N <= 100
# 1 <= Each integer value <= 10^8
# 1 <= T <= 1000

# Input Format:
# The first line contains N.
# The second line contains N integers separated by a space.
# The third line contains T.

# Output Format:
# The first line contains S or -1.

# Example Input/Output 1:
# Input:
# 4
# 87369 4012 22312 39845
# 6

# Output:
# 3903

# Explanation:
# Here N = 4 and T = 6.
# t = 1 -> 8736 4012 22312 39845 (The unit digit of the 1st integer is removed).
# t = 2 -> 8736 4012 22312 3984 (The unit digit of the 4th integer is removed).
# t = 3 -> 8736 4012 2231 3984 (The unit digit of the 3rd integer is removed).
# t = 4 -> 8736 4012 2231 398 (The unit digit of the 4th integer is removed).
# t = 5 -> 873 4012 2231 398 (The unit digit of the 1st integer is removed).
# t = 6 -> 873 401 2231 398 (The unit digit of the 2nd integer is removed).
# Now the sum of the modified integers is 3903 (873 + 401 + 2231 + 398).
# So 3903 is printed as the output.

# Example Input/Output 2:
# Input:
# 4
# 22 44 33 55
# 7

# Output:
# 5

# Explanation:
# Here N = 4 and T = 7.
# t = 1 -> 2 44 33 55
# t = 2 -> 2 4 33 55
# t = 3 -> 2 4 3 55
# t = 4 -> 2 X 3 55 (X indicates the integer to be removed)
# t = 5 -> 2 X 55 (X indicates the integer to be removed)
# t = 6 -> X 55 (X indicates the integer to be removed)
# t = 7 -> 5
# Hence 5 is printed as the output.

# Example Input/Output 3:
# Input:
# 3
# 123 456 789
# 9

# Output:
# -1




n = int(input())
arr = list(map(int,input().split()))
k = int(input())
i=0
p=0
for _ in range(k):
    while arr[i]==0:
        i += p
        if i>=n: i=0
        if i<0 : i=n-1
        if sum(arr)==0: 
            break
    x = arr[i]%10
    arr[i] = arr[i] //10
    if x%2==0:
        i += 1
        p = 1
    else:
        i -= 1
        p = -1
    if i>=n: i=0
    if i<0 : i=n-1
print(sum(arr) if sum(arr)!=0 else -1)