import coverage
import subprocess

cov = coverage.Coverage()

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.energy = 50

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")

    def eat(self, food_energy):
        self.energy += food_energy

    def sleep(self, hours):
        self.energy += 5 * hours

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Bird(Animal):
    def make_sound(self):
        return "Tweet!"

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def feed_all_animals(self, food_energy):
        for animal in self.animals:
            animal.eat(food_energy)

# Test Cases
def test_animal_creation():
    dog = Dog("Buddy", "Dog")
    assert dog.name == "Buddy"
    assert dog.species == "Dog"
    assert dog.energy == 50

def test_animal_sound():
    cat = Cat("Whiskers", "Cat")
    assert cat.make_sound() == "Meow!"

def test_animal_actions():
    dog = Dog("Max", "Dog")
    dog.eat(20)
    assert dog.energy == 70

    cat = Cat("Fluffy", "Cat")
    cat.sleep(3)
    assert cat.energy == 65

def test_bird_creation():
    bird = Bird("Sparrow", "Bird")
    assert bird.name == "Sparrow"
    assert bird.species == "Bird"
    assert bird.energy == 50

def test_zoo():
    zoo = Zoo()

    dog = Dog("Rex", "Dog")
    cat = Cat("Whiskers", "Cat")
    bird = Bird("Robin", "Bird")

    zoo.add_animal(dog)
    zoo.add_animal(cat)
    zoo.add_animal(bird)

    zoo.feed_all_animals(10)

    assert dog.energy == 60
    assert cat.energy == 60
    assert bird.energy == 60

if __name__ == "__main__":
    cov.start()
    # Run test cases
    test_animal_creation()
    test_animal_sound()
    test_animal_actions()
    test_bird_creation()
    test_zoo()
    cov.stop()

    # Save coverage data
    cov.save()

    # Use the coverage run command to execute the script and generate the report
    coverage_command = f"coverage run {__file__}"
    subprocess.run(coverage_command, shell=True)

    # Generate coverage report
    cov.report(omit=[__file__], show_missing=False)
    cov.html_report(omit=[__file__])
