# Main program for controlling a bank made up of accounts
from Bank import *

# Create an instance of the bank
oBank = Bank(hours='9 to 5',
             address='123 Main Street, Anytown, USA',
             phone='(650) 555-1212')

# Main code
while True:
    print()
    print('Press b get the balance')
    print('Press o to open a new account')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show all accounts')
    print('Press i to show information of the bank')
    print('Press q to quit')
    print('Press c to close account')
    print()

    action = input('what do you wanna do? ').casefold()[0]

    try:
        if action == 'b':
            oBank.getBalance()
        elif action == 'o':
            oBank.openAccount()
        elif action == 'd':
            oBank.Deposit()
        elif action == 'w':
            oBank.Withdraw()
        elif action == 's':
            oBank.showAccounts()
        elif action == 'i':
            oBank.showBank()
        elif action == 'c':
            oBank.closeAccount()
        elif action == 'q':
            break
        else:
            print('sorry, that was an invalid action, please try again.')
    except AbortTransaction as error:
        # Print out the text of the error message
        print(error)

print('Done')