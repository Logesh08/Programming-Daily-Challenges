# Alternate letters in uppercase
# A str‌ing (only alphabets) is passed as input. The printed output should contain alphabets in odd positions in each word in uppercase and alphabets in even positions in a word in lowercase.

# Example input and output:

# If the input is 'tREE GiVES us fruiTS', the output should be 'TrEe GiVeS Us FrUiTs'
# If the input is 'FLoweR iS beauTIFUL', the output should be 'FlOwEr Is BeAuTiFuL'






x = list(input().split())
for s in x:
    s = list(s)
    for i in range(len(s)):
        if i%2: s[i]=s[i].lower()
        else: s[i]=s[i].upper()
    print(''.join(s),end=' ')