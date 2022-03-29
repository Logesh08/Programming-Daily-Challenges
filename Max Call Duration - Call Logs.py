# Max Call Duration - Call Logs
# The program must accept the outgoing call logs of a mobile number as the input. Each call log contains the mobile number, call start time and end time. The program must print the mobile number having the maximum call duration. If there are two or more such mobile numbers having the maximum call duration, then the program must print them in the order of their occurrence.

# Boundary Condition(s):
# 2 <= N <= 50

# Input Format:
# The first line contains N.
# The next N lines, each contains the mobile number, call start time and end time separated by a space.

# Output Format:
# The lines contain the mobile number(s) having the maximum call duration.

# Example Input/Output 1:
# Input:
# 5
# 9876543210 07:08:00 07:09:32
# 9998887775 10:50:00 10:50:10
# 9876543210 10:50:45 10:55:00
# 9998887775 13:23:10 13:24:58
# 9998887775 17:05:27 17:06:40

# Output:
# 9876543210

# Explanation:
# 9876543210 (2 times) -> Total duration: 92 + 255 = 347 seconds.
# 9998887775 (3 times) -> Total duration: 10 + 108 + 73 = 191 seconds.
# The mobile number 9876543210 is having the maximum call duration.
# Hence the output is 9876543210.

# Example Input/Output 2:
# Input:
# 6
# 9876543210 07:08:00 07:09:32
# 9998887775 10:50:00 10:50:10
# 9876543210 10:50:45 10:55:00
# 9998887775 13:23:10 13:24:58
# 9998887775 17:05:27 17:06:40
# 9998887775 17:10:00 17:12:36

# Output:
# 9876543210
# 9998887775






n=int(input())
d={}
for _ in range(n):
    key,start,end = input().split()
    sh,sm,ss = map(int,start.split(':'))
    eh,em,es = map(int,end.split(':'))
    start = ss + (sm*60) + (sh*60*60)
    end = es + (em*60) + (eh*60*60)
    val = (end - start)
    if key in d.keys():
        d[key]+= val
    else:
        d[key]= val
Max = sorted(d.items(),key = lambda item: -item[1])[0][1]
for key in d.keys():
    if d[key]==Max:
        print(key)