class BankAccount:

  def __init__(self,owner,balance):
    self.owner = owner
    self.__balance = balance

  def bygetter(self):
    return self.__balance

  def bysetter(self, amount):
    if amount>=0:
       self.__balance = amount
    else:
       print("Invalid amount!")


obj = BankAccount("Hanuman",2200)

print(obj.bygetter())

obj.bysetter(54000)
print(obj.bygetter())
