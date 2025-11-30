# OBJECT ORIENTED PROGRAM
class student:                   ## class it was a blueprint to objects
    name = "ranjitha"
    age = 50
s1 = student()
print(s1.name,s1.age)


class human():
    def __init__(self,name):  # init constructor 
                               #  self it was a  method
        self.name = name
    def managing(self):
        print(f"{self.name} wish you happy many more returns of the day")

n1 = human ("dhanush")
n1.managing()


class employee():
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

harry = employee("harry","jackson",45000)
print(harry.fname,harry.lname,harry.salary)

class employee:
    def __init__(self, fname, lname, salary):

        self.fname = fname
        self.lname = lname
        self.salary = salary


    def getinfo(self):
            print(f"{self.fname} is a {self.lname} with {self.salary}")
harry = employee("harry","doctore","50000, salary")
harry.getinfo()   


        











        
