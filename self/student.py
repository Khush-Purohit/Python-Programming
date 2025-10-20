'''Q 1. Create a class 'Student' with rollno, studentName, course ,dictionary of
marks(subjectName -> marks [5]). Provide following functionalities
A. initializer
B. override __str__ method
C. accept student data
D. Print student data for given id.
E. Print Student who has failed in any subject. 

Write menu driven program to test
above functionalities.( accept records of 5 students and store those in list )
2. Write a menu driven program to maintain student information. for every student
store studetid, sname, and m1,m2,m3 marks for 3 subject. also store gpa in
student list, add a function in student class to return GPA of a student
 - Calculate GPA()
      gpa=(1/3)*m1+(1/2)*m2+(1/4)*m3

Create list to store Multiple students.
1. Display All Student
2. Search by id
3. Search by name
4. Calculate GPA of a student
5. Exit
'''


class Student:
    cnt = 1

    

    #constructor
    def __init__(self,name, course ,marks):
        self.roll = Student.cnt
        self.full_name = name
        self.course = course
        self.marks = marks
        self.gpa = self.calculate_gpa()
        Student.cnt+=1
    @property
    def get_id(self):
        return self.roll

    def __str__(self):
        return (f'Student roll number : {self.roll} name : {self.full_name} course : {self.course} marks : {self.marks} gpa : {self.gpa}')

    def get_marks(self):
        return self.marks
    
    def calculate_gpa(self):
        m1,m2,m3 = self.marks.values()
        gpa = (1/3)*m1+(1/2)*m2+(1/4)*m3
        return round(gpa,2)
    
    # def calculate_gpa(self):
    #     m1,m2,m3 = self.marks.values()

    #     return (1/3)*m1+(1/2)*m2+(1/4)*m3



class StudentUtil:
    # lst = list(Student)
    def __init__(self):
        self.lst = []
        # pass

    def add_student(self, name, course, marks):
        s1 = Student(name, course, marks)
        self.lst.append(s1)

    def print_all_student(self):
        for i in self.lst:
            print(i)

    def print_student(self,id):
        for i in self.lst:
            if(i.get_id() == id):
                print(i)
                break

    def failed_students(self):
        for i in self.lst:
            # print('printing i')
            # print(i)
            d = i.get_marks()
            for k in d.keys():
                
                # print(d[k])
                if(d[k] <= 2 ):
                    # print('printing failed i')
                    print(i)
                    break



ut = StudentUtil()

ut.add_student('a', 'CSE', {'a':1, 'b' : 3, 'c' : 4})
ut.add_student('b', 'ECE', {'a':3, 'b' : 4, 'c' : 5})
ut.add_student('c', 'EEE', {'a':1, 'b' : 5, 'c' : 5})

ut.print_all_student()
print('now printing failed students')
ut.failed_students()
# ut.print_student()


