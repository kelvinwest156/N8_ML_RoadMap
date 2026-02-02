class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!!"

    def get_age_in_dog_years(self):
        return self.age*7

    def celebrate_birthday(self):
        self.age += 1
        return f"Happy birthday {self.name}! Now {self.get_age_in_dog_years()} years old"


dog1 = Dog(name="Buddy", age=20)

print(dog1.bark())
print(dog1.get_age_in_dog_years())
print(dog1.celebrate_birthday())
print(dog1.age)