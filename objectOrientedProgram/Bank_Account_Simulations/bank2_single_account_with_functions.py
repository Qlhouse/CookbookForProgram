# Bank Version 2
# Single account

account_name = ''
account_balance = 0
account_password = ''


def new_account(name, balance, password):
    global account_name, account_balance, account_password
    account_name = name
    account_balance = balance
    account_password = password


def show():
    global account_name, account_balance, account_password
    print(f"""
        name: {account_name}
        Balance: {account_balance}
        Password: {account_password} 
    """)


def get_balance(password):
    global account_name, account_balance, account_password
    if password != account_password:
        print('Incorrect password')
        return None
    return account_balance


def deposit(amount_to_deposit, password):
    global account_name, account_balance, account_password
    if amount_to_deposit < 0:
        print('You cannot deposit a negative amount!')
        return None

    if password != account_password:
        print("Incorrect password")
        return None

    account_balance = account_balance + amount_to_deposit
    return account_balance


def withdraw(amount_to_withdraw, password):
    global account_name, account_balance, account_password

    if amount_to_withdraw < 0:
        print('You cannot withdraw a negative amount!')
        return None

    if password != account_password:
        print("Incorrect password")
        return None

    if amount_to_withdraw > account_balance:
        print('You cannot withdraw more than you have in your account')
        return None

    account_balance = account_balance - amount_to_withdraw
    return account_balance


new_account('John', 100, 'soup')  # Create an account

while True:
    print("""
    Press b to get the balance
    Press d to make a deposit 
    Press w to make a withdrawal 
    Press s to show the account 
    Press q to quit 
    """)

    action = input('What do you want to do? ')
    action = action.lower()  # Force lowercase
    action = action[0]  # Just use first letter
    print()

    if action == 'b':
        print("Get Balance: ")
        user_password = input('Please enter the password: ')
        the_balance = get_balance(user_password)
        if the_balance is not None:
            print("Your balance is: ", the_balance)

    elif action == 'd':
        print("Deposit: ")
        user_deposit_amount = input('Please enter amount of deposit: ')
        user_deposit_amount = int(user_deposit_amount)
        user_password = input('Please enter the password: ')

        new_balance = deposit(user_deposit_amount, user_password)

        if new_balance is not None:
            print("Your new balance is: ", new_balance)

    elif action == 's':
        print(f"""Show :
        'Name', {account_name}
        'Balance: ', {account_balance}
        'Pawword: ', {account_password}
        """)

    elif action == 'q':
        break

    elif action == 'w':
        print('Withdraw: ')

        user_withdraw_amount = input('Please enter the amount of withdraw: ')
        user_withdraw_amount = int(user_withdraw_amount)
        user_password = input('Please enter the password: ')

        new_balance = withdraw(user_withdraw_amount, user_password)

        if new_balance is not None:
            print("Your new balance is: ", new_balance)

print('Done')
