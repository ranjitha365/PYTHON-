#polymorphism
class Dog:
    def sound(self):
        print("DOg barks: woof!")
class cat:
    def sound(self):
        print("cat meows : meows")

for animal in (Dog(),cat()):
    animal.sound()


# method over loading
class calculator:
    def add (sef, a, b):
        print(a+b)
        c = calculator
        c.add(4,8)

class calculator:
        def add (self,a,b,c):
             print(a+b)

        def add(self,a  ,b ,c=0):
             print(a + b + c)
c = calculator
c.add(1, 2)
c.add(3, 4, 5)


