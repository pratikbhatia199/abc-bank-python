from collections import defaultdict
class Bank:
    def __init__(self):
        self.customers = set()

    def addCustomer(self, customer):
        if customer not in self.customers:
            self.customers.add(customer)
        else:
            print("Customer with name John already present")

    def customerSummary(self):
        summary = "Customer Summary"
        for customer in self.customers:
            summary = summary + "\n - " + customer.name + " (" + self._format(customer.numAccs(), "account") + ")"
        return summary

    def _format(self, number, word):
        return str(number) + " " + (word if (number == 1) else word + "s")

    def totalInterestPaid(self):
        total = 0
        for c in self.customers:
            total += c.totalInterestEarned()
        return total

    def getFirstCustomer(self):
        try:
            customerList = list(self.customers)
            return customerList[0].name
        except Exception as e:
            print(e)
            return "Error"