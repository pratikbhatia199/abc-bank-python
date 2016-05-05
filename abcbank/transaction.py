from abcbank.date_provider import  DateProvider


class Transaction:
    def __init__(self, amount):
        self.amount = amount
        self.transactionDate = DateProvider.now()