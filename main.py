
from personal_account import PersonalAccount

# account users:
if __name__ == "__main__":

    account = PersonalAccount(230102028, "Saidulaev Temir")
    account.deposit(600000)
    account.withdraw(30000)
    account.print_transaction_history()
    print(f"Current balance: {account.get_balance()}")



    account2 = PersonalAccount(230102032, "Muratov Almir")
    account2.deposit(400000)
    account2.withdraw(20000)
    print(account2)
    account2.print_transaction_history()

    # Using operator deposit and withdraw
    account + 500
    account - 200
    print(account)
