#Create a domy bank account
class BankAccount:
    def __init__(self, name, account_number, city, branch, balance=0):
        self.name = name
        self.account_number = account_number
        self.city = city
        self.branch = branch
        self.balance = balance
        self.active = True

    def display_info(self):
        if self.active:
            print(f"Account Holder: {self.name}")
            print('-----------------------------------')
            print(f"Account Number: {self.account_number}")
            print('-----------------------------------')
            print(f"City: {self.city}, Branch: {self.branch}")
            print('-----------------------------------')
            print(f"Balance: ₹{self.balance}")
        else:
            print("This account is closed!")

    def update_details(self, name=None, city=None, branch=None):
        if not self.active:
            print("Cannot update, account is closed.")
            return
        if name:
            self.name = name
        if city:
            self.city = city
        if branch:
            self.branch = branch
        print("Details updated successfully!")


    def deposit(self, amount):
        if self.active and amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully!")
        else:
            print("Invalid operation.")

    def withdraw(self, amount):
        if not self.active:
            print("Account closed, withdrawal not allowed.")
            return
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully!")
        else:
            print("Insufficient balance!")

    def transfer(self, target_account, amount):
        if not self.active:
            print("Your account is closed, cannot transfer.")
            return
        
        if amount <= self.balance and target_account.active:
            self.balance -= amount
            target_account.balance += amount
            print(f"₹{amount} transferred to {target_account.name}")
            print('-----------------------------------')
        else:
            print("Transfer failed!")

    def check_balance(self):
        if self.active:
            print(f"Current Balance: ₹{self.balance}")
        else:
            print("Account closed!")

    def calculate_interest(self, rate, years):
        if not self.active:
            print("Account closed, no interest calculation.")
            return
        interest = (self.balance * rate * years) / 100
        print(f"Interest for {years} years at {rate}% = ₹{interest}")
        return interest

    def close_account(self):
        if self.active:
            self.active = False
            print("Account closed successfully!")
        else:
            print("Account already closed.")



# Create two accounts
acc1 = BankAccount("Amit", "123456", "Delhi", "National Punjab Bank", 5000)
print('-----------------------------------')
acc2 = BankAccount("Neha", "987654", "Mumbai", "SBI", 3000)
print('----------------------------------')

acc1.display_info()
acc1.deposit(3000)
acc1.withdraw(5000)
acc1.transfer(acc2, 1500)
acc1.check_balance()
acc1.calculate_interest(5, 2)
acc1.update_details(name="Amit Singh ", city="Gurgaon")
acc1.display_info()
acc1.close_account()
acc1.withdraw(100)
print('----------------------------------------------')
acc2.display_info()
acc2.deposit(20000)
acc2.withdraw(5000)
acc2.transfer(acc2, 10000)
acc2.check_balance()
acc2.calculate_interest(2, 2)
acc2.update_details(name="Rahul singh", city="Gurgaon")
acc2.display_info()
acc2.close_account()
acc2.withdraw(1000)

# should not work after closure




















































                


    



