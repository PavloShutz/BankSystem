from decors_for_bank import save_func_info, take_taxes


class BankAccount:
    def __init__(self, name, pin: int, passport, balance=0):
        self._name = name
        if isinstance(pin, int) and len(str(pin)) == 4:
            self.__pin = pin
        else:
            raise Exception("expected valid input( pin is int, len(pin) = 4 )")
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

    def get_pin_info(self, pin):
        return self.__pin if pin else False

    def get_balance(self, pin):
        if pin == self.__pin:
            return self.__balance
        return False

    def __get_access(self, pin):
        if pin == self.__pin:
            return True
        return False

    def __change_balance(self, pin, amount_of_money):
        access = self.__get_access(pin)
        if access:
            self.__balance += amount_of_money

    def change_balance(self, terminal, pin, amount_of_money):
        if isinstance(terminal, type(ATM)):
            self.__change_balance(pin, amount_of_money)
        return "Access denied!"


class ATM:
    __full_money_amount = 150_000
    amount_of_money = __full_money_amount

    @staticmethod
    def get_balance_access(user, pin):
        if isinstance(user, BankAccount):
            access = user.get_pin_info(pin)
            if access:
                return True
        return False

    def __enter_pin(self, user):
        pin = int(input("Enter your PIN: "))
        access = self.get_balance_access(user, pin)
        return [access, pin]

    @save_func_info
    @take_taxes
    def charge_money(self, user, money_amount):
        if isinstance(user, BankAccount) and money_amount < ATM.amount_of_money:
            info = self.__enter_pin(user)
            access, pin = info[0], info[1]
            if access:
                user.change_balance(type(ATM), pin, money_amount)
                ATM.amount_of_money -= money_amount
                if ATM.amount_of_money <= 1000:
                    ATM.amount_of_money += ATM.__full_money_amount - ATM.amount_of_money
                return money_amount
            else:
                return "Wrong PIN!"

    @staticmethod
    @save_func_info
    def collect_money(money_amount):
        if money_amount < ATM.amount_of_money:
            ATM.amount_of_money -= money_amount
            if ATM.amount_of_money <= 1000:
                ATM.amount_of_money += ATM.__full_money_amount - ATM.amount_of_money
                return "Money collected!"

    @save_func_info
    @take_taxes
    def get_balance_info(self, user):
        if isinstance(user, BankAccount):
            access = self.__enter_pin(user)
            return user.get_balance(access[1]) if access else "Wrong PIN!"
