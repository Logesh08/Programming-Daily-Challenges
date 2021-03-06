# Integers Sum - Missing Digits
# The program must accept N integers as the input. For each integer X among the given N integers, the program must form an integer using the missing digits in X in descending order. Then the program must print the sum of the N resulting integers as the output.

# Boundary Condition(s):
# 1 <= N <= 100
# 1 <= Each integer value <= 10^8

# Input Format:
# The first line contains N.
# The second line contains N integers separated by a space.

# Output Format:
# The first line contains an integer representing the sum obtained based on the given conditions.

# Example Input/Output 1:
# Input:
# 4
# 4647 67865 150 321879

# Output:
# 20679392

# Explanation:
# 1st integer 4647 -> 9853210.
# 2nd integer 67865 -> 943210.
# 3rd integer 150 -> 9876432.
# 4th integer 321879 -> 6540.
# 9853210 + 943210 + 9876432 + 6540 = 20679392.

# Example Input/Output 2:
# Input:
# 6
# 16091486 66905731 21139621 94271012 30503791 51552070

# Output:
# 211852

# Explanation:
# 1st integer 16091486 -> 7532.
# 2nd integer 66905731 -> 842.
# 3rd integer 21139621 -> 87540.
# 4th integer 94271012 -> 8653.
# 5th integer 30503791 -> 8642.
# 6th integer 51552070 -> 98643.
# 7532 + 842 + 87540 + 8653 + 8642 + 98643 = 211852.





def provide(x): 
    ret="0" 
    for c in "9876543210":
        if c not in x: 
            ret+=c 
    return int(ret)


input()
print(sum (list(map( provide,input().split())) ))
