import pickle


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Метод make_sound реализован в подклассах.")

    def eat(self):
        raise NotImplementedError("Метод eat реализован в подклассах.")


class Bird(Animal):
    def __init__(self, name, age, can_fly=True):
        super().__init__(name, age)
        self.can_fly = can_fly

    def make_sound(self):
        print(f"Птица {self.name} прекрасно поет!")

    def eat(self):
        print(f"Птица {self.name} клюет зернышки.")


class Mammal(Animal):
    def __init__(self, name, age, has_milk=True):
        super().__init__(name, age)
        self.has_milk = has_milk

    def make_sound(self):
        print(f"Млекопитающее {self.name} ревёт как слон в брачный период.")

    def eat(self):
        print(f"Млекопитающее {self.name} кушает из кормушки.")


class Reptile(Animal):
    def __init__(self, name, age, is_poisonous=False):
        super().__init__(name, age)
        self.is_poisonous = is_poisonous

    def make_sound(self):
        print(f"Рептилия {self.name} не издаёт никаких звуков, затаилась.")

    def eat(self):
        print(f"Рептилия {self.name} переваривает предыдущую еду.")


class Zoo:
    def __init__(self):
        # Животные
        self.bird = Bird("Павлин", 2, True)
        self.mammal = Mammal("Кошка", 1, True)
        self.reptile = Reptile("Крокодил", 5, False)
        self.animals = [self.bird, self.mammal, self.reptile]

        # Сотрудники
        self.zookeeper = ZooKeeper("Иван")
        self.veterinarian = Veterinarian("Марина")
        self.staff = [self.zookeeper, self.veterinarian]

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff_member(self, staff_member):
        self.staff.append(staff_member)

    def animal_sounds(self):
        for animal in self.animals:
            animal.make_sound()

    def feed_animals(self):
        self.zookeeper.feed_animals(self.animals)

    def heal_animal(self, animal):
        self.veterinarian.heal_animal(animal)


class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animals(self, animals):
        for animal in animals:
            animal.eat()


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        if not isinstance(animal, Animal):
            return

        print(f"Ветеринар {self.name} лечит {animal.name}.")


def save_zoo_to_file(zoo, filename="zoo_data.pkl"):
    with open(filename, 'wb') as file:
        pickle.dump(zoo, file)


def load_zoo_from_file(filename="zoo_data.pkl"):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None


def main():
    zoo = Zoo()

    # Демонстрация работы методов
    zoo.animal_sounds()
    zoo.feed_animals()
    zoo.heal_animal(zoo.mammal)

    # Сохраняем данные зоопарка в файл
    save_zoo_to_file(zoo)

    # Загружаем данные зоопарка из файла
    loaded_zoo = load_zoo_from_file()
    if loaded_zoo:
        print("\nЗоопарк загружен из файла:")
        loaded_zoo.animal_sounds()


if __name__ == "__main__":
    main()