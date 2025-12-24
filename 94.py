# SOLID PRINCIPLES IN PYTHON

# it helps to maintainable and scalable object oriented code to make codde better#


# 1. single respponsibility principle

class student:                           #(CLASS THAT SHOULD DO ONLY ONE JOB)
    def __init__(self,name):
        self.name = name

class studentDatabase:   
     def save(self,student):
            print(f"saving {student.name} to database")
class ReportCard:
     def generate(self,student):
          print(f"generating report card for {student.name}..")

#2.open closed principles
# it means software entities(class, functions etc) should be open for extension
#  and closed for modification

# it was a good verssion code 
class Discount:
     def get_discount(self):
          return 0

class RegularCustomer(Discount):
     def get_dicount(self):
          return 10
     
class PremiumCustomer(Discount):
     def get_discount(self):
          return 20
     
# TOO : YOU CAN ADD MORE CUSTOMER TYPES BY EXTENDING. NOT MODIFYING THE EXTENDING CODE

# bad version of code
class Discount:
     def get_Discount(self, customer_type):
          if customer_type == "regular":
               return 0
          
          elif customer_type == "stranger":
               return 20
          
# LISKOV SUBSTITUTION PRINCIPLE(LSP)
# subclass shoud be able to replace their parent class without breaking the program.

# bad version of code 
class Bird:
     def fly(self):
          print("flying.....")

class penguin(Bird):
     def fly(self):
          raise NotImplementedError("penguin can't fly")

# too: penguin violates LSP because it can't actually replace Bird


#4. Interface segragation principle
# don't force a class to implement methods it does not use.
### BAD AND MOST WORST WORST EXMPLE
class worker:
     def work(self):
          pass

     def eat(self):
          pass
class Robot(worker):
     def eat(self):
          raise NotImplementedError("Robots don't eat")
     
# robot shoudn't be forced to have eat()

##good example
class workable:
     def work(self):
          pass

class Eatable:
     def eat(self):
          pass
     
class Human(workable, Eatable):
     def work(self):
          print("HUman working")

     def eat(self):
          print("Human eating")

class Robot(workable):
     def work(self):
          print("Robot working")


# Now,each class only implements the methods of really needs

#5. dependency invversion principle
# define: high level modules shoud not depend on low-level modules. Both should depend on abstracion

class InputDevices:
     def input(self):
          pass
class Keyboard(InputDevices):
     def input(self):
          return "user typing..."
class Mouse(InputDevices):
     def input(self):
          return " mouse clicked"
class computer:
     def __init__(self, device: InputDevices):
          self.device = device
          def get_input(self):
               return self.device.input()









    
          
          
          
     

    



























