class Bank:
    bank_name = "Global Bank"  # Class attribute shared across all instances
    total_accounts = 0  # Tracks total number of accounts created

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder  # Instance attribute unique to each account
        self.balance = balance
        Bank.total_accounts += 1  # Update class attribute when instance is created

    def deposit(self, amount):
        """Instance method: modifies instance state (the balance)"""
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance for {self.account_holder} is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    @classmethod
    def change_bank_name(cls, new_name):
        """Class method: modifies class state shared by all instances"""
        cls.bank_name = new_name
        print(f"Bank name changed to {cls.bank_name} for all accounts.")

    @classmethod
    def get_total_accounts(cls):
        """Class method: accesses class state"""
        print(f"Total accounts created: {cls.total_accounts}")

    @staticmethod
    def validate_account_number(account_number):
        """
        Static method: performs validation logic independent of class or instance state.
        For example, simple IBAN length check (here, assume length must be 20).
        """
        if isinstance(account_number, str) and len(account_number) == 20 and account_number.isdigit():
            print(f"Account number {account_number} is valid.")
            return True
        else:
            print(f"Account number {account_number} is invalid.")
            return False


# Using the class:

# Static method called without instance creation
Bank.validate_account_number("12345678901234567890")  # Valid
Bank.validate_account_number("12345")  # Invalid

# Instance method works on particular accounts
acc1 = Bank("Alice", 1000)
acc1.deposit(500)  # Deposit to Alice's account

acc2 = Bank("Bob")
acc2.deposit(300)  # Deposit to Bob's account

# Class method called on class or instance to change shared data
Bank.change_bank_name("Continental Bank")
acc1.change_bank_name("Worldwide Bank")  # Also works via instance

# Class method to get number of accounts created
Bank.get_total_accounts()
acc2.get_total_accounts()
