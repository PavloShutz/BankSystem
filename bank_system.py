class BankAccount:
    def __init__(self, name, pin, passport, balance=0):
        self._name = name
        self.__pin = pin
        self.__passport = passport
        self.__balance = balance
        self.__balance_access = False

    def __changed__balance_access(self):
        self.__balance_access = True
        return self.__balance_access

    def get_balance_access(self, pin):
        if pin == self.__pin:
            return self.__changed__balance_access()
        return False


class ATM:
    amount_of_money = 150_000

    def __init__(self):
        pass

    @staticmethod
    def enter_pin(user):
        pin = int(input("Enter your PIN: "))
        access = user.get_balance_access(pin)
        return access

    def charge_money(self, user, amount_of_money):
        if type(user) is BankAccount and amount_of_money < ATM.amount_of_money:
            access = self.enter_pin(user)
            if access:
                user._BankAccount__balance += amount_of_money
            else:
                return "Wrong PIN!"

    def get_balance_info(self, user):
        if type(user) is BankAccount:
            access = self.enter_pin(user)
            return user._BankAccount__balance if access else "Wrong PIN!"
