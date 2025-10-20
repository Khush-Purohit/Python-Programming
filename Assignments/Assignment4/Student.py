class Student:

    # @staticmethod
    def getGPA(self):
        return self._gpa

    @staticmethod
    def getGPAFromMarks(self,marks):
        # marks = self._marks
        gpa=0
        v = list(marks.values())
        gpa = round(((1/3)*v[0] + (1/2)*v[1] + (1/4)*v[2]),2)

        return gpa



    def __init__(self, rollNo,studentName, course, marks):
        self._rollNo = rollNo
        self._studentName = studentName
        self._course =course
        # marks are out of 100
        self._marks = marks
        self._gpa = self.getGPAFromMarks(self,marks)

    def __str__(self):
        return f'\nStudent roll :{self._rollNo} ,name :{self._studentName} ,course: {self._course}, marks: {self._marks}, gpa: {self._gpa}'
    
    def getRoll(self):
        return self._rollNo

    # @staticmethod
    def getMarks(self):
        return self._marks
    
    def getName(self):
        return self._studentName
    
    
                   




class studentData:
    # lst = []
    def __init__(self,lst):
        self.lst =[]

    def addData(self, roll, name, course, marks):
        s = Student(roll, name,course,marks )
        self.lst.append(s)

    def sendAll(self):
        for i in self.lst:
            print(i)

    def getStudent(self, rollNo):
        for i in self.lst:
            if i.getRoll() == rollNo:
                print(i)
                break

    def failedStudents(self):
        for i in self.lst:
            marks = i.getMarks()
            # print(marks)

            for k,v in marks.items():
                # for mark in v:
                if(v<35):
                    print(i)
                    break
    
    # def getStudentId(self):
    #     return self._

    def getGPAFromId(self,id):
        for i in self.lst:
            if i.getRoll() == id:
                return i.getGPA()
    

    def getStudentByName(self,nm):
        for i in self.lst:
            if(i.getName() == nm):
                # return i.getName()
                print(i)
                return


# studData = studentData()
# studData.addData(1,'aa', 'dbda', {'maths':90})
# print(studData)