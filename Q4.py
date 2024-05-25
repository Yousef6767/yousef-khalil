class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Current balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * (self.interest_rate / 100)
        self.balance += interest_amount
        print(f"Applied interest. Current balance: ${self.balance:.2f}")

    def print(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Account number: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")
        print(f"Interest rate: {self.interest_rate}%")

# Example usage
if __name__ == "__main__":
    # Create a Bank Account
    bank_account = BankAccount("554466", "Yousef khalil")
    bank_account.deposit(1000)
    bank_account.withdraw(500)

    # Create a Savings Account
    savings_account = SavingsAccount("778532", "Gafar Zayne", 2.5)
    savings_account.deposit(2000)
    savings_account.apply_interest()
    savings_account.print()