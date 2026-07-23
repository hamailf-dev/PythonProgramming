# 05 · Classes & OOP
print("\n--- Exercise 5: Classes & OOP ---")

# 5.1 — Basic class
class BankAccount:
    def _init_(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance
    
    def _str_(self):
        return f"BankAccount(owner='{self.owner}', balance={self.balance})"

# Test it
acc = BankAccount("Alice", 100)
print("5.1", acc)
acc.deposit(50)
print("5.1 After deposit:", acc)
acc.withdraw(30)
print("5.1 After withdraw:", acc)

# 5.2 — Inheritance
class SavingsAccount(BankAccount):
    def _init_(self, owner, balance=0, interest_rate=0.02):
        super()._init_(owner, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return self.balance

# Test it
sav = SavingsAccount("Bob", 200)
print("5.2", sav)
sav.add_interest()
print("5.2 After interest:", sav)

print("\n--- Exercise 5 Complete ---")