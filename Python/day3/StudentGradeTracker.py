students=[("alice",[85, 90, 78, 92]),
        ("Bob", [60, 65, 70, 75]),
        ("Charlie", [40, 45, 50, 55]),
        ("David", [95, 100, 98, 92])]

dic={}
for name, grades in students:
    dic[name]=grades
print(dic)

avg_marks={}
max_value=0
highest_avg_std=""
count=0
for name, grades in students:
    avg_marks[name]=sum(grades)/4
    if avg_marks[name]>max_value:
        max_value=avg_marks[name]
        highest_avg_std=name
    if avg_marks[name]>50:
        count=count+1
    if name=='Bob':
        print("the avg grade for bob: ",avg_marks[name])
print("avg grades of all students in dict: ",avg_marks)
print("the student with the highest avg grade: ",highest_avg_std)
print("no.of students who passed: ",count)
