# class Student:
#     college_name = "GIST"

#     # this is called default constructor 
#     def __init__(self):
#         pass
#     # this is called as parameteriezed constructor
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

# s1 = Student("sai",25)
# print(s1.name)
# print(s1.marks)
# # We can access the class varibles by using object reference 
# print(s1.college_name)

# s2 = Student("kumar",56)
# print(s2.name,s2.marks)
# # We can access the class varibles by using classname also
# print(Student.college_name)

# Create a class that takes names & marks of 3 subjects as arguments of constructor.Then create a method to print the average.
class Student:
    def __init__(self,name,tel,hin,eng):
        self.name = name
        self.sub1 = tel
        self.sub2 = hin
        self.sub3 = eng

    def get_average_value(self):
        average = (self.sub1 + self.sub2 + self.sub3) / 3
        print("Student Name is",self.name)
        print("The average value of three subjects is",average)

s1 = Student("Sai",75,80,96)
s1.get_average_value()

s2 = Student("Mahesh",99,98,96)
s2.get_average_value()
