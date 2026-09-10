class Car:

    class Engine:
        def start(self):
            print("Engine started")

    def __init__(self):
        self.engine = self.Engine()


car = Car()

car.engine.start()
