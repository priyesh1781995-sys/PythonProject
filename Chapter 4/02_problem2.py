#Q2.Write a program to accept marks of 6 students and display them in a stored manner?

marks = []

f1 = int(input("Enter Marks here: "))
marks.append(f1)
f2 = int(input("Enter Marks here: "))
marks.append(f2)
f3 = int(input("Enter Marks here: "))
marks.append(f3)
f4 = int(input("Enter Marks here: "))
marks.append(f4)
f5 = int(input("Enter Marks here: "))
marks.append(f5)
f6 = int(input("Enter Marks here: "))
marks.append(f6)

marks.sort() 

print(marks)




# The same line repets multiple times, so with the help of loop we can write in short lines as...

marks = []

for i in range(6):
    mark = int(input("Enter Marks here: "))
    marks.append(mark)

marks.sort()
print(marks) 

