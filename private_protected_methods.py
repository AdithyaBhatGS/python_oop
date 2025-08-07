class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner          # public attribute
        self._balance = balance     # protected attribute (single underscore)
        self.__pin = 1234           # private attribute (double underscore)

    def deposit(self, amount):
        self._increase_balance(amount)
        print(f"{amount} deposited. New balance: {self._balance}")

    def _increase_balance(self, amount):
        # Protected method: not for public use but accessible to subclasses
        self._balance += amount

    def __validate_pin(self, pin):
        # Private method: internal logic, not accessible outside the class normally
        return pin == self.__pin

    def withdraw(self, amount, pin):
        if self.__validate_pin(pin):
            if amount <= self._balance:
                self._balance -= amount
                print(f"{amount} withdrawn. New balance: {self._balance}")
            else:
                print("Insufficient balance")
        else:
            print("Invalid PIN")

# Usage
account = BankAccount("Alice", 1000)
account.deposit(500)          # Calls public method that uses a protected method internally

# Accessing protected attribute (possible but not recommended)
print(f"Protected balance: {account._balance}")

# Accessing private method (will raise AttributeError)
# account.__validate_pin(1234)  # Uncommenting this will cause an error

# Withdraw with pin validation using private method internally
account.withdraw(200, 1234)

# Accessing private attribute directly will cause error
# print(account.__pin)  # AttributeError

# Access via name mangling (not recommended but possible)
print(f"Private PIN via name mangling: {account._BankAccount__pin}")
