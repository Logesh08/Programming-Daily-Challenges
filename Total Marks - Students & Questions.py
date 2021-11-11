# Total Marks - Students & Questions
# In a game, there are N students standing in a row. The class teacher asks Q questions to the N students in the following order.
# 1, 2, 3, .... N-2, N-1, N, N-1, N-2, .... 3, 2, 1, 2, 3, ... N-2, N-1, N, N-1, N-2, ... and so on.
# The class teacher also awards marks to each question based on their answers. The value of N and the marks awarded for each question are passed as the input. The program must print the total marks scored by each student as the output.

# Boundary Condition(s):
# 3 <= N <= 100
# 1 <= Q <= 10^4
# 0 <= Marks for each question <= 100

# Input Format:
# The first line contains N.
# The second line contains Q.
# The third line contains Q integers separated by a space representing the marks awarded for the Q questions.

# Output Format:
# The first line contains N integers separated by a space representing the total marks scored by the N students.

# Example Input/Output 1:
# Input:
# 5
# 13
# 6 2 5 1 3 4 7 10 9 8 5 10 7

# Output:
# 15 20 17 15 10

# Explanation:
# 1st student: 6 + 9 = 15 (Q1, Q9)
# 2nd student: 2 + 10 + 8 = 20 (Q2, Q8, Q10)
# 3rd student: 5 + 7 + 5 = 17 (Q3, Q7, Q11)
# 4th student: 1 + 4 + 10 = 15 (Q4, Q6, Q12)
# 5th student: 3 + 7 = 10 (Q5, Q13)

# Example Input/Output 2:
# Input:
# 4
# 13
# 6 2 5 1 3 4 7 10 9 8 5 10 7

# Output:
# 20 26 22 9










n=int(input())
q=int(input())
l=list(map(int,input().split()))
p,t=[0]*n,0
for i in range(q):
    if t==0:ctr=0
    if t==n-1:ctr=1
    p[t]+=l[i]
    if ctr==0:t+=1
    else:t-=1
print(*p)