#BANKING MENUE BY using N OOOPS ENCAPSULATION INHERITANCE POLYMORPHISM

class Account :
    def __init__(self,id,holder_name):
        self.id = id
        self.holder_name = holder_name
        self.balance = 0              #encapsulation

# single responsiblility principles
  
def check_balance(self):
    print(f"balance: {self._balance}")
def deposit(self,amount):
    self.__balance += amount
    print(f"Deposite successfull updated balance:{self._balance}")
def withdraw(self,amount):
    if self._balance >= amount :
       self._balance -= amount
       print("withdraw succesfull. updated balance : {self._balance}")
    else:
        print("Balance is less than ask")

class savingsaccount (Account) :
    
    def calculate_interest(self):
        INTREST_RATE = 0.04
        interest = self._balance  *INTREST_RATE
        print(f"interest : {interest}")

class currentAccount(Account):
    def withdraw(self,amount):   #polymorphism
        OVERDRAFT_LIMIT = 1000
        if self._balance + OVERDRAFT_LIMIT >= amount:
           self._balance -= amount 
           print(f"withdraw successfull. updated Balance:")
        else:
            print("Ask is over limit")

class bank :
    def __init__(self,name,city):
        self.name = name
        self.city = city
        self.__accounts = {}

def create_account(self,id, holder_name,type):
    if type =="savings":
        new_account = savingsaccount(id,holder_name,type)
    elif type=="current" :
        new_account = currentAccount(id, holder_name)
    self.__account[id] = new_account
    print("Account creation successfull")
    return new_account

def get_account(self, id):
    if id not in self.__accounts:
        print("Account not found!")
        return None

    else:
        account = self.__accounts[id]
        print(f"\nID: {account.id}\nHOlder name: {account.holder_name}")
        return account


cbk = bank("chandan Bank of kaarnataka","mysore")
s1 = cbk.create_account("1","Darshan","savings")
c1 = cbk.crate_acccount("2","virat","current")
s1.deposite(1000)
c1.deposite(10)

s1.withdraw(2000)
s1.withdraw(20)

s1.calculate_interest()



     


        
    


    

    

