

'''Given the names and grades for each student in a class of n students,
store them in a nested list and print the name(s) of any student(s)
 having the second lowest grade.
Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line.

input:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

output-
Berry
Harry'''


l1=[]
n=[]
scores = set()
for _ in range(int(input())):
    name = input()
    score = float(input())
    l1.append([name,score])
    l1.sort()
    scores.add(score)
s=sorted(scores)[1]
for name,score in l1:
    if s==score:
        n.append(name)
for name in sorted(n):
    print(name)