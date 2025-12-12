# create a student class that stores 
# name 
#roll number
# marks of 3 subject

# and calculate 
#total
# average
# grade

class student:
    def __inite__(self,name,rollnumber,m1,m2,m3):
        self.name = name
        self.rollnumber = rollnumber
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def total (self):
        return self.m1 + self.m2 + self.m3 
    def average (self):
        return self.total()/3
    def grade (self):
        avg = self.average()

        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "c"
        else:
            return "D"
s1 = student ("noorvi", 101, 88, 92, 72)
print("name:",s1.name)
print("roll:",s1.roll)
print("total:",s1.total())
print("average:", s1.average())
print("grade:", s1.grade())
