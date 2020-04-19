
#object为基类
class School(object):
    def __init__(self, schoolNmae, schoolAddr):
        self.schoolNmae = schoolNmae
        self.schoolAddr = schoolAddr
        self.students = []
        self.teachers = []

    def enroll(self, stu_obj):
        print("为 %s 办理注册手续" % stu_obj.name)
        self.students.append(stu_obj)

    def hire(self, teachers_obj):
        self.teachers.append(teachers_obj)
        print("雇佣老师 %s" % teachers_obj.name)

class SchoolMember(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def introduce(self):
        pass


class Teacher(SchoolMember):
    def __init__(self, name, age, sex, salary, course):
        super(Teacher, self).__init__(name, age, sex)
        self.salary = salary
        self.course = course

    def introduce(self):
        print('''
        --------info of teacher:%s------
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        ''' % (self.name, self.name, self.age, self.sex, self.salary, self.course))

    def teach(self):
        print("%s is teaching cources [%s]" % (self.name, self.course))

class Student(SchoolMember):
    def __init__(self, name, age, sex, id, grade):
        super(Student, self).__init__(name, age, sex)
        self.id = id
        self.grade = grade

    def introduce(self):
        print('''
        --------info of student:%s------
        Name:%s
        Age:%s
        Sex:%s
        Id:%s
        Grade:%s
        ''' % (self.name, self.name, self.age, self.sex, self.id, self.grade))

    def payMoney(self, money):
        print("%s paid money for %s yuan" %(self.name, money))

sch = School("fanvil", "beijing")
t1 = Teacher("lijian", 45, "m", 2000, "sing")
t2 = Teacher("shenshen", 30, "m", 100, "dance")

s1 = Student("mcheng", "25", "f", "001", "sing")
s2 = Student("lan", "24", "m", "002", "dance")

t1.introduce()
t2.introduce()
s1.introduce()
s2.introduce()

sch.enroll(s1)
sch.enroll(s2)
sch.hire(t1)
sch.hire(t2)

print(sch.students)
print(sch.teachers)

sch.teachers[0].teach()
for stu in sch.students:
    stu.payMoney(10)