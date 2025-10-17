class Dog:
    def sound(self):
        print("Woof!")
class Cat:
    def sound(self):
        print("Meow!")
# Make objects (instances) from these classes
my_dog = Dog()
my_cat = Cat()
# Call the same method on different objects
my_dog.sound()
my_cat.sound()
