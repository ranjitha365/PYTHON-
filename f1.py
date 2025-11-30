# INSTANCE METHOD 
# 1st parameter is self

class student:
    def show(self):             #parameter
       print("this is an instance method")
s1 = student()                  #initialisation
s1.show()                       # to take a output


# class method

class student:
    school = "vghps"

    @classmethod
    def show_school(cls):             # paarameter
        print(cls.school) 
student.show_school()


# static method

class student:
    @staticmethod
    def greet():
        print("hello!sir")
student.greet()


# instance variables

class Dog:
    def __init__(self ,name,colour):
        self.name = name
        self.colour = colour
Dog1 = Dog("tommy","brown")
Dog2 = Dog("cheeku","white")
print(Dog1.name,Dog1.colour)
print(Dog2.name,Dog2.colour)

#chnging one name
Dog1.name = "max"
print(Dog1.name)               # this means one name change other name dont change 

print(Dog2.name)


# clas variable

class student:
    school_name = "green valley school"
    def __init__(self,name):
        self.name = name

    @classmethod
    def change_School(cls, new_name):
            cls.school_name = new_name

s1 = student("amith")
s2 = student("rashi")

print(s1.name)
print(s2.name)

student.change_School("blue mountain school")

print(s1.school_name)
print(s2.school_name)
    

        
    

    






    
