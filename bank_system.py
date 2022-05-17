"""Implementation of Bank system
with two classes: BankAccount and ATM.
"""

from typing import Union, Optional

from decors_for_bank import save_func_info, take_taxes
from pin_error import InvalidPinError


class BankAccount:
    """User bank account"""

    def __init__(self, name: str, pin: int,
                 passport: Union[str, int], balance: Union[int, float] = 0):
        self._name = name
        if isinstance(pin, int) and len(str(pin)) == 4:
            self.__pin = pin
        else:
            raise InvalidPinError(pin)
        self.__passport = passport
        self.__balance = balance

    @save_func_info
    def change_pin(self):
        pin = int(input("Enter PIN: "))
        if pin == self.__pin:
            new_pin = int(input("Enter new PIN: "))
            if len(str(new_pin)) == 4:
                self.__pin = new_pin
                return "PIN changed successfully!"
            return "Pin len must be 4 numbers!"
        return "Wrong PIN!"

    def get_pin_info(self, pin: int) -> Union[int, bool]:
        return self.__pin if pin else False

    def get_balance(self, pin: int) -> Union[Union[int, float], bool]:
        return self.__balance if pin == self.__pin else False

    def __get_access(self, pin: int) -> Optional[int]:
        return pin == self.__pin

    def __change_balance(self, pin: int, amount_of_money: Union[int, float]):
        if self.__get_access(pin):
            self.__balance += amount_of_money

    def change_balance(self, terminal, pin: int,
                       amount_of_money: Union[int, float]) -> Optional[str]:
        if isinstance(terminal, type(ATM)):
            self.__change_balance(pin, amount_of_money)
        return "Access denied!"


class ATM:
    __full_money_amount = 150_000.0
    amount_of_money = __full_money_amount

    @staticmethod
    def get_balance_access(user: BankAccount, pin: int) -> bool:
        return bool(isinstance(user, BankAccount) and user.get_pin_info(pin))

    def __enter_pin(self, user: BankAccount) -> list[Union[bool, int]]:
        pin = int(input("Enter your PIN: "))
        access = self.get_balance_access(user, pin)
        return [access, pin]

    @save_func_info
    @take_taxes
    def charge_money(self, user: BankAccount,
                     money_amount: Union[int, bool]) -> Union[int, str]:
        if isinstance(user, BankAccount) and \
                money_amount < ATM.amount_of_money:
            info = self.__enter_pin(user)
            access, pin = info[0], info[1]
            if access:
                user.change_balance(type(ATM), pin, money_amount)
                ATM.amount_of_money -= money_amount
                if ATM.amount_of_money <= 1000:
                    ATM.amount_of_money += \
                        ATM.__full_money_amount - ATM.amount_of_money
                return money_amount
            else:
                return "Wrong PIN!"
        return "Access denied!"

    @staticmethod
    @save_func_info
    def collect_money(money_amount: Union[int, float]) -> str:
        if money_amount < ATM.amount_of_money:
            ATM.amount_of_money -= money_amount
            if ATM.amount_of_money <= 1000:
                ATM.amount_of_money += \
                    ATM.__full_money_amount - ATM.amount_of_money
                return "Money collected!"
            return "Money collected!"
        return "You can't collect money!"

    @save_func_info
    @take_taxes
    def get_balance_info(self, user: BankAccount) \
            -> Union[Union[int, float], str]:
        if isinstance(user, BankAccount):
            access = self.__enter_pin(user)
            return user.get_balance(access[1]) if access else "Wrong PIN!"
