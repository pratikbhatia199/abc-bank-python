from nose.tools import assert_equals

from abcbank.account import Account, CHECKING, MAXI_SAVINGS, SAVINGS
from abcbank.bank import Bank
from abcbank.customer import Customer
from abcbank.date_provider import  DateProvider


def test_customer_summary():
    bank = Bank()
    john = Customer("John").openAccount(Account(CHECKING))
    bank.addCustomer(john)
    assert_equals(bank.customerSummary(),
                  "Customer Summary\n - John (1 account)")


def test_unique_customer_added():
    bank = Bank()
    john1 = Customer("John")
    bank.addCustomer(john1)
    bank.addCustomer(john1)
    assert_equals(bank.customerSummary(),
                  "Customer Summary\n - John (0 accounts)")



def test_checking_account():
    bank = Bank()
    checkingAccount = Account(CHECKING)
    bill = Customer("Bill").openAccount(checkingAccount)
    bank.addCustomer(bill)
    checkingAccount.deposit(100.0)
    assert_equals(bank.totalInterestPaid(), 0.1 * DateProvider.getTotalDaysPassedRatio())

def test_savings_account():
    bank = Bank()
    savingsAccount = Account(SAVINGS)
    bank.addCustomer(Customer("Bill").openAccount(savingsAccount))
    savingsAccount.deposit(1500.0)
    assert_equals(bank.totalInterestPaid(), savingsAccount.interestEarned())


def test_maxi_savings_account():
    bank = Bank()
    maxiSavingsAccount = Account(MAXI_SAVINGS)
    bank.addCustomer(Customer("Bill").openAccount(maxiSavingsAccount))
    maxiSavingsAccount.deposit(3000.0)
    assert_equals(bank.totalInterestPaid(), maxiSavingsAccount.interestEarned())