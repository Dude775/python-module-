# === Exercise 1 - Person ===
class Person:
    def __init__(self, name, age, city, job):
        self.name = name
        self.age = age
        self.city = city
        self.job = job

    def info(self):
        return f"{self.name}, age {self.age}, lives in {self.city}, works as {self.job}"

p1 = Person("David", 30, "Tel Aviv", "AI Specialist")
print(p1.info())


# === Exercise 2 - Car ===
class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def describe(self):
        return f"{self.color} {self.brand} {self.model} ({self.year})"

c1 = Car("Toyota", "Yaris", 2015, "White")
print(c1.describe())


# === Exercise 3 - Book ===
class Book:
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre

    def short_info(self):
        return f"{self.title} - {self.genre}"

b1 = Book("1984", "George Orwell", 328, "Dystopian")
print(b1.short_info())


# === Exercise 4 - Dog ===
class Dog:
    def __init__(self, name, age, breed, weight):
        self.name = name
        self.age = age
        self.breed = breed
        self.weight = weight

    def describe(self):
        print(f"{self.name} is a {self.age}-year-old {self.breed}, weighs {self.weight}kg")

d1 = Dog("Rex", 3, "Labrador", 30)
d1.describe()


# === Exercise 5 - Phone ===
class Phone:
    def __init__(self, brand, model, price, battery):
        self.brand = brand
        self.model = model
        self.price = price
        self.battery = battery

    def get_price(self):
        return self.price

ph1 = Phone("Samsung", "Galaxy S24", 3500, 4000)
print(ph1.get_price())


# === Exercise 6 - Student ===
class Student:
    def __init__(self, name, age, grade, school):
        self.name = name
        self.age = age
        self.grade = grade
        self.school = school

    def name_and_grade(self):
        return f"{self.name} - grade: {self.grade}"

s1 = Student("Rolf", 22, 95, "IITC")
print(s1.name_and_grade())


# === Exercise 7 - Movie ===
class Movie:
    def __init__(self, title, year, rating, duration):
        self.title = title
        self.year = year
        self.rating = rating
        self.duration = duration

    def get_rating(self):
        return self.rating

m1 = Movie("Inception", 2010, 8.8, 148)
print(m1.get_rating())


# === Exercise 8 - Laptop ===
class Laptop:
    def __init__(self, brand, ram, storage, price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.price = price

    def get_ram(self):
        return self.ram

l1 = Laptop("Lenovo", 16, 512, 4200)
print(l1.get_ram())


# === Exercise 9 - Teacher ===
class Teacher:
    def __init__(self, name, subject, experience, salary):
        self.name = name
        self.subject = subject
        self.experience = experience
        self.salary = salary

    def get_subject(self):
        return self.subject

t1 = Teacher("Lirone", "DevOps", 5, 25000)
print(t1.get_subject())


# === Exercise 10 - City ===
class City:
    def __init__(self, name, country, population, area):
        self.name = name
        self.country = country
        self.population = population
        self.area = area

    def name_and_country(self):
        return f"{self.name}, {self.country}"

city1 = City("Tel Aviv", "Israel", 460000, 52)
print(city1.name_and_country())


# === Exercise 16 - Employee ===
class Employee:
    def __init__(self, name, position, salary, years):
        self.name = name
        self.position = position
        self.salary = salary
        self.years = years

    def name_and_position(self):
        return f"{self.name} - {self.position}"

e1 = Employee("Dana", "Team Lead", 28000, 4)
print(e1.name_and_position())


# === Exercise 17 - House ===
class House:
    def __init__(self, address, rooms, price, owner):
        self.address = address
        self.rooms = rooms
        self.price = price
        self.owner = owner

    def get_price(self):
        return self.price

h1 = House("Herzl 10", 4, 2500000, "Moshe")
print(h1.get_price())


# === Exercise 18 - Computer ===
class Computer:
    def __init__(self, cpu, ram, storage, gpu):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.gpu = gpu

    def specs(self):
        return f"CPU: {self.cpu}, RAM: {self.ram}GB, Storage: {self.storage}GB, GPU: {self.gpu}"

comp1 = Computer("i7-13700K", 32, 1000, "RTX 4070")
print(comp1.specs())


# === Exercise 19 - Airplane ===
class Airplane:
    def __init__(self, model, capacity, flight_range, airline):
        self.model = model
        self.capacity = capacity
        self.flight_range = flight_range  # range הוא built-in בפייתון - לא נדרוס אותו
        self.airline = airline

    def get_model(self):
        return self.model

a1 = Airplane("Boeing 737", 180, 5500, "El Al")
print(a1.get_model())


# === Exercise 20 - GymMember ===
class GymMember:
    def __init__(self, name, age, membership_type, months_left):
        self.name = name
        self.age = age
        self.membership_type = membership_type
        self.months_left = months_left

    def get_membership(self):
        return self.membership_type

gm1 = GymMember("Yossi", 28, "Premium", 6)
print(gm1.get_membership())
