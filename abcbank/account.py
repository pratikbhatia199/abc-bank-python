from abcbank.transaction import Transaction
from abcbank.date_provider import  DateProvider

CHECKING = 0
SAVINGS = 1
MAXI_SAVINGS = 2


class Account:
    def __init__(self, accountType):
        self.accountType = accountType
        self.transactions = []

    def __hash__(self):
        return self.accountType

    def __cmp__(self):
        return object.__cmp__(self)

    def __eq__(self, rhs):
        return self.accountType == rhs.accountType

    def deposit(self, amount):
        if (amount <= 0):
            print("amount must be greater than zero")
        else:
            self.transactions.append(Transaction(amount))

    def withdraw(self, amount):
        if (amount <= 0):
            raise ValueError("amount must be greater than zero")
        else:
            self.transactions.append(Transaction(-amount))

    def interestEarned(self):
        amount = self.sumTransactions()
        if self.accountType == SAVINGS:
            if (amount <= 1000):
                return amount * 0.001
            else:
                return 1 + (amount - 1000) * 0.002

        if self.accountType == MAXI_SAVINGS:
            if not self.checkTransactionInLastTenDays():
                return amount * 0.005
        else:
            return amount * 0.001

    def sumTransactions(self):
        return sum([t.amount for t in self.transactions])

    def checkTransactionInLastTenDays(self):
        for t in self.transactions:
            if t.transactionDate >= DateProvider.tenDaysAgo():
                return False
        return True

    def transfer(self, toAccount, amount):
        if self == toAccount:
            raise ValueError("transfer between same accounts are invalid")
        if self.sumTransactions() < amount:
            raise ValueError("amount in "+ self.accountType +"< 0")
        else:
            self.withdraw(amount)
            toAccount.deposit(amount)