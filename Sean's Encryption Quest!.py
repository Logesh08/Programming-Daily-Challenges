Sean's Encryption Quest!
One day Sean's friend John wanted him to encrypt a few messages that were to be sent via a TELEGRAM group, so that everyone could see the message, but only those special people who knew decryption can actually understand it. Help Sean write a code that take input values of the type of encryption, a key, and a message to be encrypted that had something to do with the key.

Input Format:
First line containing the type of encryption X.
Second line containing the key K.
Third line containing the message M.

Output Format:
The first line contains the encrypted message.

NOTE:
The encryption process is based on the simple logic of ADDITION, that is simply adding the value of the key(/modified key) to the characters of the message to be encrypted. ONLY UPPER CASE alphabets need to be considered.
X is a number -1 or 0 or 1,
a) -1 denotes the decreasing value of the key,
b) 0 denotes the constant value of the key,
c) 1 denotes the increasing value of the key
d) In case of invalid input value of X simply display “Invalid Input”.

If the input value of K is less than or equal to 0, make the initial value of K as 1

Boundary Conditions:
The maximum length of the message M is 200 and it's minimum length is 1

Example Input/Output 01:
Input:
1
2
SUMMER

Output:
UXQRKY

Explanation: Every time the key is used on a character its value is incremented by 1

Example Input/Output 02:
Input:
-1
6
HOLIDAY

Output:
NTPLFBY

Explanation: Every time the key is used on a character its value is decremented by 1

Example Input/Output 03:
Input:
0
2
ENTERTAINMENT

Output:
GPVGTVCKPOGPV

Example Input/Output 04:
Input:
-1
1
ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ

Output:
AZYXWVUTSRQPONMLKJIHGFEDCBAZYXWVUTSRQPONMLKJIHGFEDCBAZYXWVUTSRQPONMLKJIHGFEDCBAZYXWVUT










typee = int(input())
key = int(input())
s = input().strip()
if typee not in [1,0,-1]:
    print('Invalid Input')
    exit()
if key==0: key=typee
for c in s:
    o = ord(c)+key
    key+=typee
    print(chr( ((o - ord('A'))%26) + ord('A') ),end='')