#To create the BankAccount class
class bank:
    def __init__(self):
        self.bal=0 #Initialize balance to 0
        print("Welcome to the SBI")

    def deposit(self):
        amt=float(input("Enter amount to be Deposited:"))
        self.bal+=amt
        print("\ndeposited amount:",amt)

    def Withdraw(self):
        amt=float(input("Enter amount to be Withdraw:"))
        if self.bal>=amt:
           self.bal-=amt
           print("\n You Withdraw:",amt)
        else:
           print("\n Insufficient balance")

    def display(self):
        print("\nNet Available balance=",self.bal)

#driver code
s= bank()#Create an object of BankAccount

s.deposit() #Deposit money
s.Withdraw() #Withdraw money
s.display() #Display balance












