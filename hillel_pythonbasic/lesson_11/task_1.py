import uuid
from decimal import Decimal
import datetime


class BankAccount:
    def __init__(self, account_name, balance=0):
        self.account_name = account_name
        self.id = str(uuid.uuid4())
        self.balance = Decimal(balance)
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += Decimal(amount)
            self._add_transaction(amount, "Депозит")
            print("Депозит на суму", amount, "здійснено.")
        else:
            print("Сума депозиту повинна бути більше нуля.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= Decimal(amount)
            self._add_transaction(amount, "Виведення")
            print("Виведення на суму", amount, "здійснено.")
        else:
            print("Недостатньо коштів або некоректна сума для виведення.")

    def get_balance(self):
        return self.balance

    def _add_transaction(self, amount, transaction_type):
        transaction = {
            "amount": Decimal(amount),
            "type": transaction_type,
            "date": datetime.datetime.now()
        }
        self.transactions.append(transaction)

        if transaction_type == "Депозит":
            self.balance += Decimal(amount) * Decimal("0.99")  # Додати банківську комісію

    def print_transactions(self):
        print("Транзакції:")
        for transaction in self.transactions:
            print("Тип:", transaction["type"])
            print("Сума:", transaction["amount"])
            print("Дата:", transaction["date"])
            print()


account = BankAccount("John Doe", 1000)

account.deposit(500)
account.withdraw(300)
account.deposit(2000)
account.withdraw(1500)

print("Поточний баланс:", account.get_balance())

account.print_transactions()
