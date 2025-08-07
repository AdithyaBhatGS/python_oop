class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner_name= owner.name
        print(f"Dog created: {self.name}, Breed: {self.breed}, Owner: {self.owner_name}")
    
    def bark(self):
        print(f"{self.name} is barking")

    def breed_name(self):
        print(f"The breed of the dog is {self.breed}")

class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

owner1 = Owner("Alice", 30, "123 Dog St")       

dog1 = Dog("Buddy", "Golden Retriever", owner1)

print(dog1)