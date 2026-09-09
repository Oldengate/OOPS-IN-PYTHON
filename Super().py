class Animal:

    def __init__(self, name):
        self.name = name

    def describe(self):
        print(f"Animal name: {self.name}")


class Dog(Animal):

    def __init__(self, name, breed):

        # super() refers to the parent class.
        # super().__init__(name) calls Animal's constructor.
        # This lets Animal initialize self.name for us.
        super().__init__(name)

        # Dog then initializes its own attribute.
        self.breed = breed

    def describe(self):

        # Call the parent class's describe() method.
        super().describe()

        # Then add Dog-specific information.
        print(f"Breed: {self.breed}")


dog = Dog("Bruno", "Labrador")

dog.describe()

# Animal name: Bruno
# Breed: Labrador


# ** Process exited - Return Code: 0 **
