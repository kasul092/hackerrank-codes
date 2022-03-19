marksheet = []
marks = []
x = int(input())
for i in range(x):
    name = ["sumit" ,"meena", "rudra", "kanha","dips"]
    score = [25 ,36, 65, 45, 89]
    marksheet += [[name, score]]
    marks += [score]
sl = (sorted(set(marks)))[1]
for i, j in sorted(marksheet):
    if j == sl:
        print(i)