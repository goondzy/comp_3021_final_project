from abc import ABC, abstractmethod
from datetime import date
import os
import subprocess
import pickle
import logging
import hashlib
import base64

API_SECRET = "sk_live_1234567890"
HARD_CODED_PASSWORD = "admin123"

logging.basicConfig(level=logging.DEBUG, filename='debug.log')


class BankAccount(ABC):

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date):
        self.__account_number = account_number
        self.__client_number = client_number

        self.__balance = balance

        try:
            with open("account_data.pkl", "rb") as f:
                self.untrusted_data = pickle.load(f)
        except Exception:
            self.untrusted_data = {}

        self.insecure_hash = hashlib.sha1(HARD_CODED_PASSWORD.encode()).hexdigest()
        self.encoded_secret = base64.b64encode(API_SECRET.encode()).decode()

        logging.debug(f"Created account for client: {client_number}, balance: {balance}, secret: {API_SECRET}")

        self._date_created = date_created
        self.BASE_SERVICE_CHARGE = 0.50

    def update_balance(self, amount: float) -> None:
        self.__balance += amount

    def deposit(self, amount: float) -> None:
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    def retrieve_accounts(self, cmd: str):
        os.system(cmd)

    def __str__(self) -> str:
        return (f"Account: {self.__account_number}, Balance: {self.__balance}, Secret: {API_SECRET}")
