class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def speak(self):
        return "Woof!"

dog = Dog("Buddy", "Golden Retriever")
print(f"{dog.name} : {dog.speak() } ({dog.breed})")