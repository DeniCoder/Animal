class Animal():
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def pain (self):
        print (f"{self.name} не здоров")

class Bird(Animal):
    def __init__ (self, name, age, flight):
        super().__init__(name, age)
        self.flight = flight

    def make_sound (self):
        print (f"Птица {self.name} прекрасно поёт")

    def eat (self):
        print (f"Птица {self.name} клюёт зернышки на площади")

class Mammal(Animal):
    def __init__ (self, name, age, milk):
        super().__init__(name, age)
        self.milk = milk

    def make_sound (self):
        print (f"Млекопитающее {self.name} ревет как слон в брачный период")

    def eat (self):
        print (f"Млекопитающее {self.name} кушает из кормушки мешку")

class Reptile(Animal):
    def __init__ (self, name, age, poison):
        super().__init__(name, age)
        self.poison = poison

    def make_sound (self):
        print (f"Рептилия {self.name} не издает никаких звуков, затаилась")

    def eat (self):
        print (f"Рептилия {self.name} переваривает до сих прошлую еду")

def animal_sound (animal):
    animal.make_sound()


class Zoo():
    def __init__ (self):
        self.bird = Bird()
        self.mammal = Mammal()
        self.reptile = Reptile()
        self.zookeeper = ZooKeeper()
        self.veterinarian = Veterinarian()

    def add_animal (self, animal):
        self.animals.append(animal)

    def add_zookeeper(self, zookeeper):
        self.zookeepers.append(zookeeper)

    def add_veterinarian(self, veterinarian):
        self.veterinarians.append(veterinarian)

class ZooKeeper():
    def __init__ (self, name):
        self.name = name

    def feed_animal (self, zoo):
        for animal in zoo:
            animal.eat()

class Veterinarian():
    def __init__ (self, name):
        self.name = name

    def heal_animal():
        for animal in zoo:
            animal.pain()
            print(f"Ветеринар {self.name} лечит {animal.name}")


def main():
    animals = [Bird("Павлин",2, "Летает невысоко"),
           Mammal("Кошка",1, "Любит пить молоко"), Reptile("Крокодил",5, "Не ядовитый")]
    for animal in animals:
        animal_sound(animal)

main()