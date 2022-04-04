# Move to Beginning - Operations Count
# The program must accept a string S and two integers X, Y as the input. The program must perform the following two operations alternately on the given string S until the string becomes the original string.
# - Move the last X characters to the beginning.
# - Move the last Y characters to the beginning.
# Finally, the program must print the number of operations performed on the given string S as the output.

# Boundary Condition(s):
# 1 <= Length of S <= 100
# 1 <= X, Y <= Length of S

# Input Format:
# The first line contains S.
# The second line contains X and Y separated by a space.

# Output Format:
# The first line contains an integer representing the number of operations performed on the given string S.

# Example Input/Output 1:
# Input:
# high
# 1 2

# Output:
# 3

# Explanation:
# Here X = 1 and Y = 2.
# 1st operation: high -> hhig
# 2nd operation: hhig -> ighh
# 3rd operation: ighh -> high

# Example Input/Output 2:
# Input:
# SkillRack
# 3 1

# Output:
# 13

# Explanation:
# Here X = 3 and Y = 1.
# 1st operation: SkillRack -> ackSkillR
# 2nd operation: ackSkillR -> RackSkill
# 3rd operation: RackSkill -> illRackSk
# 4th operation: illRackSk -> killRackS
# 5th operation: killRackS -> ckSkillRa
# 6th operation: ckSkillRa -> ackSkillR
# 7th operation: ackSkillR -> llRackSki
# 8th operation: llRackSki -> illRackSk
# 9th operation: illRackSk -> kSkillRac
# 10th operation: kSkillRac -> ckSkillRa
# 11th operation: ckSkillRa -> lRackSkil
# 12th operation: lRackSkil -> llRackSki
# 13th operation: llRackSki -> SkillRack













s = input().strip()
x, y = map(int,input().split())
cont = 0
t=s
while cont==0 or s!=t:
    if cont%2==0:
        i = -x
    else:
        i = -y
    s = s[i:]+s[:i]
    cont+=1
print(cont)