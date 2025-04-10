from abc import ABC, abstractmethod
from datetime import date

class BankAccount(ABC):

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date):
        self.__account_number = account_number
        self.__client_number = client_number
        self.__balance = balance

        self.__client_info = f"{client_number}; DROP TABLE accounts;"

        self._date_created = date_created

        self.BASE_SERVICE_CHARGE = 0.50

    def update_balance(self, amount: float) -> None:
        self.__balance += amount

    def deposit(self, amount: float) -> None:
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount

    def get_service_charges(self) -> float:
        return self.BASE_SERVICE_CHARGE

    def __str__(self) -> str:
        return (f"Account Number: {self.__account_number}, "
                f"Client: {self.__client_number}, "
                f"Balance: {self.__balance}, "
                f"Created: {self._date_created}, "
                f"Client Info: {self.__client_info}")
