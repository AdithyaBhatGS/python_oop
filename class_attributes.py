

class Person:

    user_count = 0  # class attribute

    def __init__(self, name, age,email):
        self.name = name
        self.age = age
        self.email = email  # instance attribute
        Person.user_count += 1
    
    def display_user_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Email: {self.email}")


smith = Person("Smith", 25, "smith@outlook.com")
smith.display_user_info()

james = Person("James", 28, "james@gmail.com")
james.display_user_info()

# Accessing class attribute
print(f"Total users created: {Person.user_count}")