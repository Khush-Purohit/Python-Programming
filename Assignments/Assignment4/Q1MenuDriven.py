from Student import studentData
lst = []
stud = studentData(lst)

while(True):
    print('\n 1. Add student \n','2. Show all students \n','3. Show a student with id \n','4. Show failed students \n','5. Get GPA of student \n','6. Get student by name \n','7. Quit \n')

    ch = int(input("Enter choice in integer:"))

    match ch:
        case 1:
            rollNo = int(input("Enter roll number: "))
            nm = input("Enter name: ")
            course = input("Enter course: ")
            marks = eval(input("Enter a dictionary of marks: "))

            stud.addData(rollNo, nm, course, marks)

        case 2:
            stud.sendAll()

        case 3:
            id = int(input("Enter id of student which is to be shown: "))

            stud.getStudent(id)

        case 4:
            stud.failedStudents()
        
        case 5:
            # get gpa of a student
            id = int(input("Enter the roll no of student: "))
            print(f"GPA of the student is {stud.getGPAFromId(id)}")

        case 6:
            nm = input("Enter the name of student: ")
            print(f'\nStudent details are:')
            stud.getStudentByName(nm)

        case 7:
            break

        case _:
            print("Enter a valid choice")

