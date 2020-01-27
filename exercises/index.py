class Car:
    wheels = 4

    def __init__(self):
        self.mil = 10
        self.com = "Tesla"


c1 = Car()
c2 = Car()

c1.mil = 8
Car.wheels = 5
c2.wheels = 3

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)


class Student:
    school = "Maxwell"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    # Accessors
    def get_m1(self):
        return self.m1
    # Mutator
    def set_m1(self, value):
        self.m1 = value

    # Class method
    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is Student class... in abc module")


s1 = Student(34, 43, 53)
s2 = Student(34, 45, 43)

print(s1.avg())
print(Student.getSchool())

Student.info()
