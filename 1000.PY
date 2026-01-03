# BANKING MENEU
# 1.creating an aaccount
# 2.Deposite money
# 3.withdraw money
# 4.check balance
# exit the system
 

class BankAccount :                           # fisrt defining class

    def __init__(self,name,Balance=0):         # # build constructor
        self.name = name                        # initialization
        self.Balance = Balance 
    def deposite(self,amount):
        self.Balance += amount
        print("amount deposited successsfully")

#Account1  = BankAccount("Noorvi",1000)         # only for my reference
#Account1.deposite(500)


    def withdraw(self,amount):
        if amount <= self.Balance:
            self.Balance -= amount
            print("amount withdraw successfuly")
        else :
            ("insufficient balance")
#account = BankAccount("Noorvi",1000)          # just for an reference
#account.withdraw(10)
    def CheckBalance(self):
        print("account holder:", self.name)
        print("current Balance:", self.Balance)

name = input("Eneter account holder name:")
account = BankAccount(name)

while True:
    print("n _ _ _BankMenue_ _ _")
    print("1.Deposite")
    print("2.withdrw")
    print("3.checkbalance")
    print("4.exit")

choice = int(input("Enetr your choice"))


if choice == 1:
    amt = int(input("Enter your deposite"))
    account.deposit(amt)
elif choice == 2:
    amt = int(input("Enter withdraw amount:"))

elif choice == 3:
    account.checkBalance()

elif choice == 4:
    print("Thankyou for using the bank system")

else:
    print("invalid choice")





















