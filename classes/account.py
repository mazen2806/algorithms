import logging
import pytz

from datetime import datetime
from collections import namedtuple

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

Transaction = namedtuple('Transaction', ['amount', 'type', 'date'])


class Account:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance
        self.history = []

    def deposit(self, amount):
        self._balance += amount
        logger.info(f'Current balance deposited: {self._balance}')

        self._update_history(amount, 'deposited')

    def withdraw(self, amount):
        self._balance -= amount
        logger.info(f'Current balance withdrawn: {self._balance}')

        self._update_history(amount, 'withdrawn')

    def show_history(self):
        logger.info(f'Show account history for {self.name}')
        for transaction in self.history:
            logger.info(f'{transaction.amount}$ {transaction.type} at {transaction.date}')

    def _update_history(self, amount, transaction_type):
        transaction_date = pytz.utc.localize(datetime.utcnow()).astimezone().isoformat()
        transaction = Transaction(amount, transaction_type, transaction_date)
        self.history.append(transaction)


if __name__ == '__main__':
    account = Account('Jesicca', 100)
    account.deposit(420)
    account.withdraw(300)
    account.show_history()
