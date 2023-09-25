class BankAccount:
    def _init_(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print("Deposited ₹{}. New balance: ₹{}".format(amount, self.__account_balance))
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            print("Withdrew ₹{}. New balance: ₹{}".format(amount, self.__account_balance))
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_balance(self):
        print("Account balance for {} (Account #{}): ₹{}".format(
            self._account_holder_name, self.account_number, self._account_balance))

# Example usage:
account = BankAccount("12345", "John Doe", 1000.0)

account.deposit(500)
account.withdraw(200)
account.display_balance()
