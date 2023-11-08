n = int(input("Enter the number of the students: "))
dict_1 = {}
for i in range(n):
    
    a = input("Enter the name of the student: ")
    b = input("Enter the marks of the student: ")
    marks_of_student = [int(x) for x in b.split()]

    dict_1[a] = marks_of_student

name = input("Enter the name of the student you want info about: ")
if name in dict_1:
    marks = dict_1[name]
    length = len(marks)
    sum_of_marks = sum(marks)
    Average = sum_of_marks/length
    print(Average)
else:
    print("Invalid info!!")