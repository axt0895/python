class Account:
    def __init__(self, account_num, account_name, account_type, balance) -> None:
        self.account_num = account_num
        self.account_name = account_name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print('The deposit amount must be a positive balance')

    def withdraw(self, amount):
        if amount > 0:
            if amount >= self.balance:
                print('Balance insufficient')
            else:
                self.balance -= amount
        else:
            print('Cannot withdraw a negative balance')

    def get_balance(self):
        print(f'The current balance is {self.balance}')


class SavingsAccount(Account):
    def __init__(self, account_num, account_name, account_type, balance = 0, interest_rate = 0.02):
        super().__init__(account_num, account_name, account_type, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate


class CheckingsAccount(Account):
    def __init__(self, account_num, account_name, account_type, balance = 0, overdraft_limit = 0) -> None:
        super().__init__(account_num, account_name, account_type, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0:
            if amount < self.balance:
                print(f'{amount} withdrawn from the bank')
                self.balance -= amount
            else:
                print('There is not enough balance in the account')
        else:
            print('Cannot withdraw from a negative balance')


class Bank:
    def __init__(self) -> None:
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_account(self, account_num):
        for account in self.accounts:
            if account_num == account.account_num:
                return self.accounts
            else:
                print('No account found with given number ')

    '''def transfer_amount(self, from_account, destination_account, amount):
        from_account = self.get_account(from_account)
        destination_account = self.get_account(destination_account)
        if amount
    '''

'''
# Create a bank instance
bank = Bank()

# Create accounts
#savings_account = SavingsAccount(account_number="SA123", owner="Alice", balance=1000, interest_rate=0.05)
#checking_account = CheckingAccount(account_number="CA123", owner="Bob", balance=500, overdraft_limit=200)

# Add accounts to the bank
bank.add_account(savings_account)
bank.add_account(checking_account)

# Deposit money
savings_account.deposit(200)
checking_account.deposit(150)

# Withdraw money
savings_account.withdraw(100)
checking_account.withdraw(600)  # Overdraft allowed

# Apply interest to savings account
savings_account.apply_interest()

# Transfer money between accounts
bank.transfer("SA123", "CA123", 300)

# Get account balances
print(f"Savings Account Balance: {savings_account.get_balance()}")
print(f"Checking Account Balance: {checking_account.get_balance()}")
'''