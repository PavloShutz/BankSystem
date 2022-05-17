"""Bank system"""

from bank_system import BankAccount, ATM

pin = int(input("Create your pin: "))
passport = input("Please, write your passport data: ")
name = input("Your name: ")

text = """
----------------
| Bank Program |
----------------

Choose an option:
1) Your balance
2) Charge your balance
3) Collect money from ATM
4) Change your pin
5) Quit
"""

atm = ATM()
bank_account = BankAccount(name, pin, passport)

while True:
    print(text)
    option = int(input("Enter a number to choose an option: "))
    if option == 1:
        print(f"Your balance is: ${atm.get_balance_info(bank_account)}")
    elif option == 2:
        money_amount = float(input("How much money "
                                   "do you want to charge?\n-->"))
        print("Your balance was charged with "
              f"${atm.charge_money(bank_account, money_amount)}")
    elif option == 3:
        amount_of_money = float(input("How much money do "
                                      "you need to collect from ATM?\n-->"))
        atm.collect_money(amount_of_money)
    elif option == 4:
        bank_account.change_pin()
    elif option == 5:
        print("Quited!")
        break
    else:
        print("Incorrect input!")
