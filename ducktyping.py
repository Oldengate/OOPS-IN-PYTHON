#"If it looks like a duck, swims like a duck, and quacks like a duck, then it's probably a duck."->polymorphism
class Duck:  
    
    def quack(self):
        print("Duck: Quack!")

class Person:
    def quack(self):
        print("Person: I can quack too!")


def make_it_quack(thing):
    thing.quack()


duck = Duck()
person = Person()

make_it_quack(duck)
make_it_quack(person)

# Duck: Quack!
# Person: I can quack too!


# ** Process exited - Return Code: 0 **
