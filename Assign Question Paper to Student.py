# Assign Question Paper to Student
# A class teacher has 26 sets of question papers named from A to Z. He wants to conduct a test for his class students. Each student has a registration number. He assigns a question paper to each student based on the following condition.
# - Find the sum of all the digits in the registration number. If the sum is within the range 1-26, then the corresponding question paper set is assigned to the student. Else the sum of the digits is calculated again and again till the sum falls within the range 1-26, and then the corresponding question paper set is assigned to the student.
# The program must accept an integer R representing the registration number of a student as the input. The program must print the name of the question paper set assigned to the student as the output.

# Boundary Condition(s):
# 1 <= R <= 10^9

# Input Format:
# The first line contains R.

# Output Format:
# The first line contains an alphabet representing the name of the question paper set assigned to the student.

# Example Input/Output 1:
# Input:
# 100954

# Output:
# S

# Explanation:
# The sum of digits in 100954 is 19.
# The 19th alphabet is S, which is assigned to the student.
# Hence the output is S.

# Example Input/Output 2:
# Input:
# 9223399

# Output:
# J

# Explanation:
# The sum of digits in 9223399 is 37, which is not in the range 1-26.
# So the sum of digits in 37 is 10.
# The 10th alphabet is J, which is assigned to the student.
# Hence the output is J.











n = int(input())
while True:
    Sum = 0
    for i in str(n):
        Sum+=int(i)
    n = Sum
    if n<27: break
print(chr(64 + n))