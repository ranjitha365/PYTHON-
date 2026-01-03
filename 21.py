

# adding by using a mgic method
class student:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,other):
        return self.marks + other.marks
    

s1 = student(40)
s2 = student(43)

print(s1+s2)



#substracting by using a logic method

class count:
    def __init__(self, sweets):
        self.sweets = sweets

    def __sub__(self,other):

        return self.sweets - other.sweets
s1 = count(25)
s2 = count(20)
print(s1 - s2)


# multiplying by using a magic method

class count:
    def __init__(self,count):
        self.count = count

    def __mul__(self,other):
       return  self.count * other.count
    

s1 = count(50)
s2 = count(45)

print(s1*s2)


 #deviding by using a magic method

 
class count:
    def __init__(self,count):
        self.count = count

    def __truediv__(self,other):
       return  self.count / other.count
    

s1 = count(4)
s2 = count(2)

print(s1/s2)


s
   


