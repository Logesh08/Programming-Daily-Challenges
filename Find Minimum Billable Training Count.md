Find Minimum Billable Training Count
As the demand for knowing Japanese language is increasing in Software Services industry (due to increase in projects from Japan), a software company decides to teach Japanese to N employees. An expert in Japanese language is hired and is designated as the ROOT mentor. Under the ROOT mentor, there are certain employees who belong to level1. Under each of these level1 employees, certain number of employees are assigned and they belong to level2. This process is repeated till all the N employees are accounted for.

So the structure is like a ROOT mentor will have level1 mentees. These level1 mentees can inturn mentor level2 mentees. The level2 mentees can inturn mentor level3 mentees and so on.

But certain employees among these N employees are already fluent in Japanese and they do not need training. Also there is a special offer that if a specific employee is trained (and billed), his immediate mentor and his immediate mentees can attend the training free of cost. So the program  must find and print the minimum biilable training count so that all the employees who are not fluent in Japanese can be trained using this special offer.

Note: Always the ROOT mentor is fluent in Japanese. But if need arises to make the training count minimum he can be considered as a billable training employee. The employee id of the ROOT mentor is 0. The employee id of the other employee is from 1 to N-1

Input Format:
First line contains N.
Next N-1 lines contain two integer values separated by a space- 1)employee id of the mentor and 2) 1 or 0 indicating if the employee is fluent in Japanese or not.

Output Format:
First line contains the minimum billable training count

Boundary Conditions:
1 <= N <= 100000

Example Input/Output 1:
Input:
11
0 1
1 0
2 0
3 0
4 0
4 0
6 1
2 0
8 1
8 0


Output:
2

Explanation:

<img src="./src/japanesetraining.png"/>

The red colored employee ids are those who do not know Japanese.
So when we train Employee 4, using the special offer 3,5,6 get free training.
When we train Employee 8, using the special offer 2 and 10 get free training.
Now all the employees who do not know Japanese are accounted for the training.
So the minimum billable training count is 2.

