from nose.tools import assert_equals

from abcbank.account import Account, CHECKING, MAXI_SAVINGS, SAVINGS
from abcbank.bank import Bank
from abcbank.customer import Customer
from abcbank.date_provider import  DateProvider
from datetime import datetime

def check_transfer_account():
    checkingAccount = Account(CHECKING)
    savingsAccount = Account(SAVINGS)
    henry = Customer("Henry").openAccount(checkingAccount).openAccount(savingsAccount)
    checkingAccount.deposit(100.0)
    savingsAccount.deposit(4000.0)
    savingsAccount.transfer(checkingAccount, 100)
    henry.getStatement()
    assert_equals(henry.getStatement(), 'Statement for Henry\n\n'
                                        'Checking Account\n  deposit $100.00\n '
                                        ' deposit $100.00\nTotal $200.00\n\nSavings Account\n '
                                        ' deposit $4000.00\n  withdrawal $100.00\nT'
                                        'otal $3900.00\n\nTotal In All Accounts $4100.00')

def test_checking_account():
    bank = Bank()
    checkingAccount = Account(CHECKING)
    bill = Customer("Bill").openAccount(checkingAccount)
    bank.addCustomer(bill)
    checkingAccount.deposit(100.0)
    assert_equals(checkingAccount.interestEarned(), 0.1 * DateProvider.getTotalDaysPassedRatio())

def test_savings_account():
    bank = Bank()
    savingsAccount = Account(SAVINGS)
    bank.addCustomer(Customer("Bill").openAccount(savingsAccount))
    savingsAccount.deposit(1500.0)
    assert_equals(savingsAccount.interestEarned(), savingsAccount.getSavingsAccountGT1000(1500) )


def test_check_transaction_in_last_10_days():
    bank = Bank()
    maxiSavingsAccount = Account(MAXI_SAVINGS)
    bank.addCustomer(Customer("Bill").openAccount(maxiSavingsAccount))
    maxiSavingsAccount.deposit(3000.0)
    assert_equals(maxiSavingsAccount.transactions[0].amount, 3000)
    assert_equals(maxiSavingsAccount.transactions[0].transactionDate.year, DateProvider.now().year)
    assert_equals(maxiSavingsAccount.transactions[0].transactionDate.month, DateProvider.now().month)
    assert_equals(maxiSavingsAccount.transactions[0].transactionDate.day, DateProvider.now().day)
    assert_equals(maxiSavingsAccount.transactions[0].transactionDate >= DateProvider.tenDaysAgo(), True)
    assert_equals(maxiSavingsAccount.checkTransactionInLastTenDays(), True)


def test_maxi_savings_account():
    bank = Bank()
    maxiSavingsAccount = Account(MAXI_SAVINGS)
    bank.addCustomer(Customer("Bill").openAccount(maxiSavingsAccount))
    maxiSavingsAccount.deposit(3000.0)
    assert_equals(maxiSavingsAccount.checkTransactionInLastTenDays(), True)
    assert_equals(3000 * 0.001 * DateProvider.getTotalDaysPassedRatio(), maxiSavingsAccount.interestEarned())