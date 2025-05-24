# OOP => OBJECT ORIENTED PROGRAMMING

class BankAccount():
    def __init__(self, ownername):
        # self = {}   #### self ke through object banayein ge self ek khali object hai.
        self.ownername = ownername
        # self = {ownername:"Rizwan"}
        self.balance = 5000000
        # self = {ownername:"Rizwan", balance = 500000}
        
# #  OOP ka ek ye beneifit bhi he ke Jitni bank functunality he class ke hi under rakhein ge...  

### Uper only nuqsha banaaya he abb object banayein ge......
 

Account1 = BankAccount("Rizwan")
print(Account1.ownername)
Account2 = BankAccount("Ali Asghar")
print(Account2.balance)

# deposit functionality add

class BankAccount():
    def __init__(self, ownername):
        self.ownername = ownername
        self.balance = 5000000

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")


Account1 = BankAccount("Rizwan")
print(Account1.ownername)
Account1.deposit(1000)
Account2 = BankAccount("Ali Asghar")
print(Account2.balance)




# withdraw functionality add
class BankAccount():
    def __init__(self, ownername):
        self.ownername = ownername
        self.balance = 5000000
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
    
Account1 = BankAccount("Rizwan")
print(Account1.ownername)
Account1.deposit(1000)
Account1.withdraw(1000)




# get detail functionality add 
class BankAccount():
    def __init__(self, ownername):
        self.ownername = ownername
        self.balance = 6000
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

    def get_details(self):
        print(f"Account Owner: {self.ownername}")
        print(f"Account Balance: {self.balance}")

Account1 = BankAccount("Alice")
print(Account1.ownername)
Account1.deposit(4000)
Account1.withdraw(1000)
Account1.get_details()






