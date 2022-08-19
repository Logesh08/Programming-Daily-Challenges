# Queries of Library

# The program must accept N queries from a library as input. Each query has + or - followed by an user id. If the query starts with +, then borrow a book from the library. If the query starts with -, then return a book to the library. The program must print the user id(s) having the most number of books in hand at the end.
# Note: If more than one user id have the same most number of books in hand, then print their user id(s) in descending order.

# Boundary Condition(s):
# 1 <= N <= 100
# 1 <= value of user id(s) <= 9999

# Input Format:
# The first line contains the value of N.
# The next N lines contain a query, each query consisting of a character and an integer.

# Output Format:
# The first line contains a list of integer(s) each separated by a space. 

# Example Input/Output 1:
# Input:
# 7
# +45
# +23
# -23
# +56
# +45
# -45
# -45

# Output:
# 56

# Explanation:
# Only the user id 56 has to return a book to the library. Hence the output is 56.

# Example Input/Output 2:
# Input:
# 10
# +421
# +421
# +156
# +945
# -945
# +156
# +945
# +945
# +689
# +556

# Output:
# 945 421 156

# Explanation:
# The user id 421 has to return 2 books to the library.
# The user id 156 has to return 2 books to the library.
# The user id 945 has to return 2 books to the library.
# The user id 689 has to return a book to the library.
# The user id 556 has to return a book to the library.
# The user ids 421 156 945 has the same number of books in hand. So print the user ids in descending order.
# Hence the output is 945 421 156








users = {}
n = int(input())
for _ in range(n):
    i = int(input())
    if i>0:
        users[i] = users.get(i,0) + 1 
    else:
        users[-i] -= 1
users = sorted(users.items(), key = lambda x: x[1])
max = users[-1][-1]
ans = []
for i in users[::-1]:
    if i[-1]==max:
        ans.append(i[0])
    else:
        break
print(*sorted(ans,reverse = True))