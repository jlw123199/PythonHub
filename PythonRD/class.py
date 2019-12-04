
# This ia calss definition example in python

class Person:
    def __init__(self):
        self.name = "human"
        self.age = 1

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


class Student(Person):
    def __init__(self, grade):
        super(Student,self).__init__()
        self.grade = grade


    def getGrade(self):
        return self.grade

class Teacher(Person):
    def __init__(self,educationBackground):
        super(Teacher,self).__init__()
        self.educationBackground = educationBackground

if __name__ == '__main__':
    s1 = Student(7)
    print( s1.getName() , s1.getGrade() ,s1.getAge(),sep ='---', end='\n')

    teacher = Teacher("Master")
    print(teacher.getName(), teacher.educationBackground, teacher.getAge(), sep='---', end='\n')