# Version 3
# Any number of accounts - with a list of dictionaries

import this


account_list = []


# [TODO] How to do: subfunction terminate the parent function
def authenticate(account_number):
    if account_number > len(account_list):
        print("You gave an illegal account number!")
        return None


def new_account(name, balance, password):
    global account_list
    new_account_dict = {'name': name, 'balance': balance, 'password': password}
    account_list.append(new_account_dict)


def show(account_number):
    # global account_list
    print("Account: ", account_number)
    authenticate(account_number)

    this_account_dict = account_list[account_number]
    print(f"""
        name: {this_account_dict["name"]}
        Balance: {this_account_dict["balance"]}
        Password: {this_account_dict["password"]} 
    """)


def get_balance(account_number, password):
    global account_list
    authenticate(account_number)
    this_account_dict = account_list[account_number]
    if password != this_account_dict['password']:
        print('Incorrect password')
        return None
    return this_account_dict['balance']


def deposit(account_number, amount_to_deposit, password):
    global account_list
    authenticate(account_number)
    this_account_dict = account_list[account_number]
    if amount_to_deposit < 0:
        print('You cannot deposit a negative amount!')
        return None

    if password != this_account_dict['password']:
        print("Incorrect password")
        return None

    this_account_dict['balance'] += amount_to_deposit
    return this_account_dict['balance']


def withdraw(account_number, amount_to_withdraw, password):
    global account_list
    authenticate(account_number)
    this_account_dict = account_list[account_number]

    if amount_to_withdraw < 0:
        print('You cannot withdraw a negative amount!')
        return None

    if password != this_account_dict['password']:
        print("Incorrect password")
        return None

    if amount_to_withdraw > this_account_dict['balance']:
        print('You cannot withdraw more than you have in your account')
        return None

    this_account_dict['balance'] -= amount_to_withdraw
    return this_account_dict['balance']


# Create two sample accounts
print("Joe's account is account number: ", len(account_list))
new_account("Joe", 100, "soup")

print("Mary's account is account number: ", len(account_list))
new_account("Mary", 12345, "nuts")

while True:
    print("""
    Press b to get the balance
    Press d to make a deposit 
    Press n to create a new account
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
        user_account_number = input("Please enter your account number: ")
        user_account_number = int(user_account_number)
        user_password = input('Please enter the password: ')
        the_balance = get_balance(user_account_number, user_password)
        if the_balance is not None:
            print("Your balance is: ", the_balance)

    elif action == 'd':
        print("Deposit: ")
        user_account_number = input("Please enter your account number: ")
        user_account_number = int(user_account_number)
        user_deposit_amount = input('Please enter amount of deposit: ')
        user_deposit_amount = int(user_deposit_amount)
        user_password = input('Please enter the password: ')

        new_balance = deposit(user_account_number,
                              user_deposit_amount, user_password)

        if new_balance is not None:
            print("Your new balance is: ", new_balance)

    elif action == 's':
        print("Show :")
        user_account_number = input("Please enter your account number: ")
        user_account_number = int(user_account_number)
        show(user_account_number)

    elif action == 'q':
        break

    elif action == 'n':
        print("New Account:")
        user_name = input("What is your name? ")
        user_starting_amount = input(
            "What is the amount of your initial deposit? ")
        user_starting_amount = int(user_starting_amount)
        user_password = input(
            "What password would you like to use for this account? ")

        user_account_number = len(account_list)
        new_account(user_name, user_starting_amount, user_password)
        print("Your new account number is: ", user_account_number)

    elif action == 'w':
        print('Withdraw: ')
        user_account_number = input("Please enter your account number: ")
        user_account_number = int(user_account_number)
        user_withdraw_amount = input('Please enter the amount of withdraw: ')
        user_withdraw_amount = int(user_withdraw_amount)
        user_password = input('Please enter the password: ')

        new_balance = withdraw(user_account_number,
                               user_withdraw_amount, user_password)

        if new_balance is not None:
            print("Your new balance is: ", new_balance)

print('Done')
