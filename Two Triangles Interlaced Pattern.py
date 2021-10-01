# Two Triangles Interlaced Pattern
# The program must accept two even integers X and Y as the input. The integer X represents the size of the inverted asterisks triangle pattern. The integer Y represents the size the hash symbols triangle pattern. The program must interlace the two triangles and print the interlaced triangles pattern as shown in the Example Input/Output section.

# Boundary Condition(s):
# 4 <= X, Y <= 100

# Input Format:
# The first line contains X and Y separated by a space.

# Output Format:
# The first M lines(where M represents the maximum value between X and Y) contains the pattern as shown in the Example Input/Output section.

# Example Input/Output 1:
# Input:
# 6 10

# Output:
# ----* * *#* * *
# -----* *#*#* *
# ------*#*#*#*
# ------#*#*#*#
# -----# #*#*# #
# ----# # #*# # #
# ---# # # # # # #
# --# # # # # # # #
# -# # # # # # # # #
# # # # # # # # # # #

# Explanation:
# Here X = 6 and Y = 10.
# The size of the inverted asterisks triangle is 6.
# The size of the hash symbols triangle is 10.
# So they are interlaced and printed as the output.
# The hyphens are printed instead of empty spaces before each row.

# Example Input/Output 2:
# Input:
# 6 4

# Output:
# * * * * * *
# -* * * * *
# --* *#* *
# ---*#*#*
# ---#*#*#
# --# #*# #

# Example Input/Output 3:
# Input:
# 8 8

# Output:
# * * * *#* * * * 
# -* * *#*#* * * 
# --* *#*#*#* * 
# ---*#*#*#*#* 
# ---#*#*#*#*# 
# --# #*#*#*# # 
# -# # #*#*# # # 
# # # # #*# # # # 






X,Y=map(int,input().split())
K=max(X,Y)
asterisk=X 
if Y>X:
    hashSymp=1
else:
    hashSymp=Y-X+1
for row in range(1,K+1):
    if hashSymp>=asterisk:
        hyphen = K - hashSymp
    else:
        hyphen = K - asterisk 
    print('-'*hyphen,end="")
    if asterisk>0 and hashSymp<=0:
        currRow=list("* "*asterisk)
    elif hashSymp>0 and asterisk<=0:
        currRow=list("# "*hashSymp)
    elif hashSymp>0 and asterisk>0:
        if hashSymp>=asterisk:
            borderHash=(hashSymp-asterisk)//2
            currRow=list("# "*borderHash + "#*"*asterisk + "# "*(borderHash+1))
        else:
            borderAst=(asterisk-hashSymp)//2
            currRow=list("* "*borderAst + "*#"*hashSymp + "* "*(borderAst+1))
    
    asterisk-=1
    hashSymp+=1
    print("".join(currRow))
