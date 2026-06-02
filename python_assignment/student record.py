stu={}

i=int(input("enter the number of students: "))
for j in range(i):
    name=input("enter the name of student: ")
    marks=int(input("enter the marks of student: "))
    stu[name]=marks

print(stu)