# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some generic animal sound"

# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # Call the parent class constructor
        super().__init__(name)
        self.breed = breed
    
    # Override the speak method
    def speak(self):
        return "Woof!"

# Create an instance of Dog
dog = Dog("Buddy", "Golden Retriever")
print(dog.name)   # Output: Buddy
print(dog.breed)  # Output: Golden Retriever
print(dog.speak())  # Output: Woof!
