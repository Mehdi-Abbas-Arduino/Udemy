class Animal():
    def __init__(self) -> None:
        print("Animal Created")
    def whoami(self):
        print("I am an Animal")
    def eat(self):
        print("I am eating")

myanimal = Animal()

# Inheritance
# All atrributes and properties are inherited 
class Dog(Animal):
    def __init__(self) -> None:
        Animal.__init__(self)
        print("Dog created")

my = Dog()
print(my.whoami())