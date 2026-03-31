# === Lab 1.0 - Animal Inheritance Hierarchy ===

# חלק 1 - מחלקת אב
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} makes a sound"


# חלק 2 - Dog
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    # דריסה של speak - הכלב נובח במקום צליל כללי
    def speak(self):
        return f"{self.name} says: Woof!"

    def fetch(self):
        return f"{self.name} is fetching the ball"


# חלק 3 - Cat
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        return f"{self.name} says: Meow!"

    def purr(self):
        return f"{self.name} is purring"


# חלק 4 - Bird
class Bird(Animal):
    def __init__(self, name, age, can_fly):
        super().__init__(name, age)
        self.can_fly = can_fly

    def speak(self):
        return f"{self.name} says: Tweet tweet!"

    def tweet(self):
        return f"{self.name} is tweeting a song"


# חלק 5 - Fish
class Fish(Animal):
    def __init__(self, name, age, water_type):
        super().__init__(name, age)
        self.water_type = water_type

    def speak(self):
        return f"{self.name} says: Blub blub!"

    def swim(self):
        return f"{self.name} is swimming in {self.water_type} water"


# חלק 6 - Horse
class Horse(Animal):
    def __init__(self, name, age, speed):
        super().__init__(name, age)
        self.speed = speed

    def speak(self):
        return f"{self.name} says: Neigh!"

    def gallop(self):
        return f"{self.name} is galloping at {self.speed} km/h"


# === חלק 7 - בדיקות ===
dog = Dog("Rex", 3, "Labrador")
cat = Cat("Whiskers", 2, "Orange")
bird = Bird("Tweety", 1, True)
fish = Fish("Nemo", 1, "salt")
horse = Horse("Spirit", 5, 60)

# speak - כל חיה מדברת אחרת (זו הדריסה בפעולה)
print(dog.speak())
print(cat.speak())
print(bird.speak())
print(fish.speak())
print(horse.speak())

# מתודות ייחודיות - כל חיה עושה משהו אחר
print(dog.fetch())
print(cat.purr())
print(bird.tweet())
print(fish.swim())
print(horse.gallop())
