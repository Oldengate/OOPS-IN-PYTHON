class Engine:
    def start(self):
        print("Engine started")


class Car:
    # Composition:
    # Composition is a strong HAS-A relationship where one class
    # owns an object of another class, and the contained object's
    # lifetime is dependent on the containing object.
    #
    # The Car creates its own Engine, so Engine is a part of Car.

    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()


# Creating a Car automatically creates its Engine.
car = Car()

car.start_car()
