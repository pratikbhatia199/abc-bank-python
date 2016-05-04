from abcbank.account import CHECKING, SAVINGS, MAXI_SAVINGS

class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = set()

    def __hash__(self):
        return abs(hash(self.name)) % (10 ** 8)

    def __cmp__(self):
        return object.__cmp__(self)

    def __eq__(self, rhs):
        return self.name == rhs.name

    def openAccount(self, account):
        if account not in self.accounts:
            self.accounts.add(account)
            return self
        else:
            ValueError("account of type "+ account.name + "already exists for customer")

    def numAccs(self):
        return len(self.accounts)

    def totalInterestEarned(self):
        return sum([a.interestEarned() for a in self.accounts])

    # This method gets a statement
    def getStatement(self):
        # JIRA-123 Change by Joe Bloggs 29/7/1988 start
        statement = None  # reset statement to null here
        # JIRA-123 Change by Joe Bloggs 29/7/1988 end
        totalAcrossAllAccounts = sum([a.sumTransactions() for a in self.accounts])
        statement = "Statement for %s" % self.name
        for account in self.accounts:
            statement = statement + self.statementForAccount(account)
        statement = statement + "\n\nTotal In All Accounts " + _toDollars(totalAcrossAllAccounts)
        return statement

    def statementForAccount(self, account):
        accountType = "\n\n\n"
        if account.accountType == CHECKING:
            accountType = "\n\nChecking Account\n"
        if account.accountType == SAVINGS:
            accountType = "\n\nSavings Account\n"
        if account.accountType == MAXI_SAVINGS:
            accountType = "\n\nMaxi Savings Account\n"
        transactionSummary = [self.withdrawalOrDepositText(t) + " " + _toDollars(abs(t.amount))
                              for t in account.transactions]
        transactionSummary = "  " + "\n  ".join(transactionSummary) + "\n"
        totalSummary = "Total " + _toDollars(sum([t.amount for t in account.transactions]))
        return accountType + transactionSummary + totalSummary

    def withdrawalOrDepositText(self, transaction):
        if transaction.amount < 0:
            return "withdrawal"
        elif transaction.amount > 0:
            return "deposit"
        else:
            return "N/A"


def _toDollars(number):
    return "${:1.2f}".format(number)
