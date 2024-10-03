class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printname(self):
        print(self.name)
    
    def change_name(self, new_name):
        self.name = new_name
        print(f"The new name is now {self.name}")



#Use the Person class to create an object, and then execute the printname method:







































class Student(Person):
    def __init__(self, name, age, school):
        Person.__init__(self, name, age)
        self.school = school
        print(self.name)



obj = Student("Luke", 22, "UC")







        
