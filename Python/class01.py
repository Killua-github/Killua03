class Student:
    def avg(self):
        print((80 + 70) / 2)

a001 = Student()
a001.avg()

class Student:
    def avg(self, math, english):
        print((math + english) / 2)

a001 = Student()
a001.avg(80, 70)
a001.avg(30, 70)

a001.name = "sato"
print(a001.name)

class Student:
    def __init__(self):
        self.name = ""
    def avg(self, math, english):
        print((math + english) / 2)

a001 = Student()
a001.name = "sato"
print(a001.name)

a002 = Student()
a002.name = "tanaka"
print(a002.name)

class Student:
    def __init__(self, name):
        self.name = name
    def avg(self, math, english):
        print((math + english) / 2)

a001 = Student("sato")
print(a001.name)

a002 = Student("tanaka")
print(a002.name)
