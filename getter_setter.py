class Person:
    def __init__(self, name, salary, age, email):
        self.name = name
        self.salary = salary
        self.age = age
        self.__email = email  # private attribute

    # @property decorator for getter
    @property
    def email(self):
        return self.__email

    # @property.setter for setter where property = email
    @email.setter
    def email(self, email):
        if "@" not in email:
            raise ValueError("Invalid email address")
        self.__email = email

paul = Person("Paul", 50000, 30, "paul@gmail.com")

# Setting the private property using setter
paul.email = "paul.outlook.com"

# Accessing private property through getter
print(paul.email)