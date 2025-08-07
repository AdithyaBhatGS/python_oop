class Person:
    def __init__(self, name, age, email, password):
        self.name = name
        self.age = age
        self._email = email
        self.__password = password


obj1 = Person("Alice", 30, "alice@gmail.com", "alice123")

# Accessing protected attribute
print(obj1._email)


# This will raise an AttributeError since __password is private 
print(obj1.__password)  


