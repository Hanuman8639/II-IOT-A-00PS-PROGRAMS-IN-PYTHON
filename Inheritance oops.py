# Single Inheritance
class A:

   def displayA(self):
     print("Inheritance A Class")

class B(A):

   def displayB(self):
     print("Inheritance B Class")

class C(B):

   def displayC(self):
     print("Inheritance C Class")

obj = C()
obj.displayA()
obj.displayB()
obj.displayC()
