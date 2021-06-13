
class Animal:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def speak(self):
        print(
            f"Hi, my name is {self.name}, I am {self.__class__.__name__} of age {self.age}, {self.breed} by breed and I sleep during the {self.sleeps_when}")

    def make_sound(self):
        print(f"As a {self.__class__.__name__}, I {self.sound}.")


class Cat(Animal):
    ''' A class of Cat that inherites from the class of Animals.
    Properties:
        name
        age
        breed
    Methods:
        speak
        make_sound 

    To Use:
    >>> willi = Cat("Willi", 3, "Kitty")
    >>> willi.speak()
    Hi, my name is Willi, I am Cat of age 3, Kitty by breed and I sleep during the Day
    >>> willi.make_sound()
    As a Cat, I Meow.

    '''

    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)
        self.sleeps_when = "Day"
        self.sound = "Meow"


class Dog(Animal):
    ''' A class of Dog that inherites from the class of Animals.
    Properties:
        name
        age
        breed
    Methods:
        speak
        make_sound

    To Use:
    >>> tim = Dog("Tim", 5, "Rotteweler")
    >>> tim.speak()
    Hi, my name is Tim, I am Dog of age 5, Rotteweller by breed and I sleep during the Night
    >>> tim.make_sound()
    As a Dog, I Bark.

    '''

    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)
        self.sleeps_when = "Night"
        self.sound = "Bark"

# Example of usage.


tim = Dog("Tim", 5, "Rotteweller")
tim.speak()
tim.make_sound()

willi = Cat("Willi", 3, "Kitty")
willi.speak()
willi.make_sound()
