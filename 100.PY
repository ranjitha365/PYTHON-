# by using oops building calculator

class calculator:
    def add(self, a,b):
        return a + b 
    def sub(self, a,b):
        return a - b
    def mul(self,a,b):
        return a* b 

    def div(sself, a, b):
        if b!= 0:
            return a/b
        
        else:
            return " division not possible "
        
calc = calculator()
while True:
    print(" 1.addition ")
    print("2. substraction")
    print("3.multipliaction")
    print("4.Division")
    print("5.Exit")

    choice = int(input("Enter your choice "))
    if choice == 5:
        print("Exit")
    else:
        a = int(input("Enter your first numer:"))
        b = int(input("Enter your second number:"))

        if choice == 1:
          
          print("Result =", calc.add(a,b))

        elif choice == 2:
          print("Result =", calc.sub(a,b))

        elif choice == 3:
          print("result =", calc.mul(a,b))
        elif choice == 4:
          print("result=",calc.div(a,b))
        else:
          print("invaliid choice ")
    


    
















































































