class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print(f"Dog created: {self.name}, Breed: {self.breed}")

    def bark(self):
        print(f"{self.name} is barking")

    def breed_name(self):
        print(f"The breed of the dog is {self.breed}")

dog_breeds = ["French Bulldog", "Labrador Retriever", "Golden Retriever"]
dog_names = ["tofu", "pofu", "mofu"]

tofu = Dog(dog_names[0], dog_breeds[0])
pofu = Dog(dog_names[1], dog_breeds[1])
mofu = Dog(dog_names[2], dog_breeds[2])

