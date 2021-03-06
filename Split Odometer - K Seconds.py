# Split Odometer - K Seconds
# The program must accept a string S containing only digits as the input. The length of the string S is always divisible by 3. The string S represents the state of a split odometer which runs based on the following conditions.
# - Every three digits in the odometer represent a value or parameter.
# - Every second, every 3rd digit in the odometer increases by 1.
# - Once the 3rd digit reaches 0, then the 2nd digit in the odometer increases by 1.
# - Once the 2nd digit reaches 0, then the 1st digit in the odometer increases by 1.
# The program must print the state of the odometer for the next K seconds from the given state as the output. The value of K is also passed as the input.

# Boundary Condition(s):
# 3 <= Length of S <= 99
# 1 <= X <= 10^4

# Input Format:
# The first line contains S.
# The second line contains K.

# Output Format:
# The first K lines contain the state of the odometer for the next K seconds from the given state.

# Example Input/Output 1:
# Input:
# 655087291
# 15

# Output:
# 656088292
# 657089293
# 658090294
# 659091295
# 660092296
# 661093297
# 662094298
# 663095299
# 664096300
# 665097301
# 666098302
# 667099303
# 668100304
# 669101305
# 670102306

# Explanation:
# Here the given string is 655087291 and the value of K is 15.
# The states of the odometer for the next 15 seconds are printed.

# Example Input/Output 2:
# Input:
# 997005
# 7

# Output:
# 998006
# 999007
# 000008
# 001009
# 002010
# 003011
# 004012





s=input().strip();l=[]
for i in range(0,len(s),3):
    l.append(int(s[i:i+3]))
for i in range(int(input().strip())):
    for j in range(len(l)):
        l[j]+=1
        if l[j]>999:
            l[j]=0
    for k in l:
        if k<10:
            print("00",k,sep="",end="")
        elif k<100:
            print("0",k,sep="",end="")
        else:
            print(k,end="")
    print()