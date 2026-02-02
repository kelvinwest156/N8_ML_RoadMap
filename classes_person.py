class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduction(self):
        return f"Hello there, my name is {self.name}. I am {self.age}years old and I come from {self.city}"

    def birthday(self):
        self.age += 1
        return f"{self.name} is now {self.age}years old"


person1 = Person("Max", 22, "California")
person2 = Person("Kim", 31, "Spintex")

print(person1.introduction())
print(person1.birthday())
print("")
print(person2.introduction())
print(person2.birthday())