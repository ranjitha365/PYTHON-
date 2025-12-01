

# abstraction method   # it is a method of hiding a complex inner working of an object
class car:
    def engine_start(self):
        print("car is started")
    def brake(self):
        print("stop car")

car = car()
car.engine_start()
car.brake()

# ENCAPSULATION (protets data from external interface and misues, improving security and maintainability)
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    def deposite(self,amount):
        if amount>0 :
            self.__balance += amount

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("insufficient balance")

    def get_balance(self):
        return self.__balance
    
acc = BankAccount(500)
acc.deposite(300)
acc.withdraw(200)
print(acc.get_balance())












































































































           

        





    


    
    
        
    

    






    
