# Cycle Tour
# Hector has planned a cycle tour through the mountains. His tour consists of N checkpoints, numbered from 1 to N in the order he will visit them. The ith checkpoint has a height of Hi.
# A checkpoint is a peak if it is not the 1st checkpoint or the Nth checkpoint, and the height of the checkpoint is strictly greater than the checkpoint immediately before it and the checkpoint immediately after it.
# Please help Hector find out the number of peaks.

# The program must accept T test cases, where each test case contains N integers representing the heights of the N checkpoints. For each test case, the program must print the number of peaks in his cycle tour.

# Boundary Condition(s):
# 1 <= T <= 100, T is the total number of test cases.
# 3 <= N <= 100
# 1 <= Hi <= 100

# Input Format:
# The first line contains T, followed by T test cases.
# Each test case contains the input as below.
# - The first line contains N.
# - The second line contains N integers separated by a space.

# Output Format:
# The first T lines, each contains an integer representing the number of peaks in Hector's cycle tour.

# Example Input/Output 1:
# Input:
# 4
# 3
# 10 20 15
# 4
# 8 8 8 8
# 5
# 20 80 30 80 20
# 3
# 100 30 100

# Output:
# 1
# 0
# 2
# 0

# Explanation:
# For the 1st test case: The 2nd checkpoint is the only peak.
# For the 2nd test case: No peaks.
# For the 3rd test case: The 2nd and 4th checkpoints are the peaks.
# For the 4th test case: No peaks.

# Example Input/Output 2:
# Input:
# 10
# 10
# 66 61 60 87 34 52 40 41 100 32
# 8
# 79 37 61 71 4 95 36 33
# 4
# 13 14 74 96
# 3
# 71 75 92
# 3
# 80 20 6
# 10
# 66 21 42 88 6 96 23 14 36 41
# 8
# 27 91 64 78 71 49 100 59
# 5
# 85 78 6 53 49
# 7
# 71 67 73 3 27 97 49
# 9
# 34 24 71 83 28 16 74 29 18

# Output:
# 3
# 2
# 0
# 0
# 0
# 2
# 3
# 1
# 2
# 2









for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    peaks = 0
    for i in range(1,n-1):
        if arr[i-1]<arr[i] and arr[i+1]<arr[i]:
            peaks+=1
    print(peaks)