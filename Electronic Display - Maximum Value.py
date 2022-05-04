# Electronic Display - Maximum Value
# In a four-digit electronic display, each digit is displayed using seven segments. The program must accept an integer N representing the number of segments to display an integer X. The program must print the maximum possible four-digit integer X that can be displayed using N segments as the output.
# The number of segments required to display each digit is given below.
# 0 - 6
# 1 - 2
# 2 - 5
# 3 - 5
# 4 - 4
# 5 - 5
# 6 - 6
# 7 - 3
# 8 - 7
# 9 - 6

# Boundary Condition(s):
# 8 <= N <= 28

# Input Format:
# The first line contains N.

# Output Format:
# The first line contains X.

# Example Input/Output 1:
# Input:
# 13

# Output:
# 9711

# Explanation:
# Here N = 13.
# The maximum possible four-digit integer that can be displayed using 13 segments is 9711 (9+7+1+1 = 13).

# Example Input/Output 2:
# Input:
# 10

# Output:
# 7711

# Example Input/Output 3:
# Input:
# 18

# Output:
# 9977







n = int(input());s=n
arr = { 6:9 , 3:7 , 5:5, 4:4 , 2: 1 , 7:8}
def get_dictKeys(val):
    for key,value in arr.items():
        if val == value: 
            return key 
p = 0  
ans = [] 
while p!=4: 
    for key in arr.keys(): 
        if (key+(3-p)*2)<=n: 
            ans.append(arr[key])  
            n -= key 
            break 
    p+=1 
m = sorted(ans)
ans = sorted(ans) 
if m[0]!= 9 and m[1]==m[2] and m[2]==m[3] and m[3]==9:
    ans[0] = arr[s-(6*3)] 
else:
    for i in range(n):
        ans[i] = arr[ get_dictKeys(ans[i]) +1 ]
print(*sorted(ans) [::-1], sep='')