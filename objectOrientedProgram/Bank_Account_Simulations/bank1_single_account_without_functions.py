# Bank Version 1
# Single account

account_name = 'Joe'
account_balance = 100
account_password = 'soup'

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
        if user_password != account_password:
            print("Incorrect password")
        else:
            print("Your balance is: ", account_balance)

    elif action == 'd':
        print("Deposit: ")
        user_deposit_amount = input('Please enter amount of deposit: ')
        user_deposit_amount = int(user_deposit_amount)
        user_password = input('Please enter the password: ')

        if user_deposit_amount < 0:
            print("You cannot deposit a negative amount!")

        elif user_password != account_password:
            print("Incorrect passrod")

        else:  # OK
            account_balance = account_balance + user_deposit_amount
            print("Your new balance is: ", account_balance)

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

        if user_withdraw_amount < 0:
            print("You cannot withdraw a negative amount")

        elif user_password != account_password:
            print("Incorrect passrod for this account")

        elif user_withdraw_amount > account_balance:
            print("You cannot withdraw more than you have in your account")

        else:  # OK
            account_balance = account_balance - user_withdraw_amount
            print("Your new balance is: ", account_balance)

print('Done')
