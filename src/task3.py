
class Animal:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def speak(self):
        print(
            f"Hi, my name is {self.name}, I am {self.age} years old, I am a {self.breed} breed and I sleep during the {self.sleeps_when}")


class Cat(Animal):
    def __init__(self):
        self.sleeps_when = "Day"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)
        self.sleeps_when = "Night"


tim = Dog("Tim", 5, "Rotteweller")
tim.speak()
