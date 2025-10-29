# Base class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def sound(self):
        print("Some animal sound")

    def info(self):
        print(f"Name: {self.name}, Species: {self.species}")


# Subclasses
class Lion(Animal):
    def __init__(self, name):
        super().__init__(name, "Lion")

    def sound(self):
        print("Roar!")


class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name, "Elephant")

    def sound(self):
        print("Trumpet!")


class Snake(Animal):
    def __init__(self, name):
        super().__init__(name, "Snake")

    def sound(self):
        print("Hiss!")


# Zoo class
class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def display_info(self):
        print(f"The zoo has {len(self.animals)} animals:")
        for animal in self.animals:
            animal.info()

    def make_all_sounds(self):
        print("\nAnimal sounds in the zoo:")
        for animal in self.animals:
            animal.sound()


# --- Example usage ---
zoo = Zoo()

lion = Lion("Simba")
elephant = Elephant("Dumbo")
snake = Snake("Kaa")

zoo.add_animal(lion)
zoo.add_animal(elephant)
zoo.add_animal(snake)

zoo.display_info()
zoo.make_all_sounds()
