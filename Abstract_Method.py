from abc import ABC, abstractmethod

# ABC = Abstract Base Class
# A class that contains one or more abstract methods
# is used as a blueprint for its child classes.
class Animal(ABC):

    # Abstract method:
    # We declare WHAT the child class must do,
    # but we don't provide the actual implementation here.
    @abstractmethod
    def make_sound(self):
        pass


# Dog inherits from Animal
class Dog(Animal):

    # Dog MUST implement make_sound()
    def make_sound(self):
        print("Dog: Woof!")


# Cat also inherits from Animal
class Cat(Animal):

    # Cat MUST implement make_sound()
    def make_sound(self):
        print("Cat: Meow!")


# Creating objects of the child classes
dog = Dog()
cat = Cat()

dog.make_sound()
cat.make_sound()

# Dog: Woof!
# Cat: Meow!


# ** Process exited - Return Code: 0 **
