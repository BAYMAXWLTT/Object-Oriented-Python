# Bank that manages a dictionary of accounts
# Functionalities: open/close an account  withdraw/deposit   get balance  show account/bank's information

from Account import *


class Bank():

    def __init__(self, hours, address, phone):
        self.accountsDict = {
        }  # key-value pairs in the form: accountNumber (int) - Account (Account object)
        self.nextAccountNumber = 0
        self.hours = hours
        self.address = address
        self.phone = phone

    def askForValidAccountNumber(self):
        accountNumber = input('enter your account number: ')
        try:
            accountNumber = int(accountNumber)
        except ValueError:
            raise AbortTransaction('the account number must be an integer')

        if accountNumber < 0:
            raise AbortTransaction('the account number must be non-negative')

        if accountNumber not in self.accountsDict.keys():
            raise AbortTransaction('There is not account numbered ' +
                                   str(accountNumber))
        return accountNumber

    def askForValidPassword(self, account):
        accountPassword = input('enter your password: ')
        try:
            account.checkPasswordMatch(accountPassword)
        except AbortTransaction:
            raise AbortTransaction('Incorrect password for this account')

        return accountPassword

    def getUsersAccount(self):
        accountNumber = self.askForValidAccountNumber()
        oAccount = self.accountsDict[accountNumber]
        self.askForValidPassword(account=oAccount)
        return accountNumber, oAccount

    def openAccount(self):
        print('*** Open Account ***')
        accountName = input('enter your new account\' name: ')
        accountStartingBalance = input(
            'enter your new account\'s starting balance: ')
        accountPassword = input('enter your new account\'s password: ')
        oAccount = Account(name=accountName,
                           balance=accountStartingBalance,
                           password=accountPassword)
        newAccountNumber = self.nextAccountNumber
        self.accountsDict[newAccountNumber] = oAccount
        self.nextAccountNumber += 1
        print('your new account is successfully created! ')

    def closeAccount(self):
        print('*** Close Account ***')
        accountNumber, oAccount = self.getUsersAccount()
        print('the balance of the account to be deleted is ',
              oAccount.getBalance())
        self.accountsDict.pop(accountNumber)
        print('your account is now closed')

    def Withdraw(self):
        print('*** Withdraw ***')
        _, oAccount = self.getUsersAccount()
        amountToWithdraw = input('enter the amount to withdraw: ')
        newBalance = oAccount.withdraw(amountToWithdraw)
        print('withdraw: ', amountToWithdraw)
        print('your new balance: ', newBalance)

    def Deposit(self):
        print('*** Deposit ***')
        _, oAccount = self.getUsersAccount()
        amountToDeposit = input('enter the amount to deposit: ')
        newBalance = oAccount.deposit(amountToDeposit)
        print('deposit: ', amountToDeposit)
        print('your new balance: ', newBalance)

    def getBalance(self):
        print('*** Get Balance ***')
        _, oAccount = self.getUsersAccount()
        print('your balance is ', oAccount.getBalance())

    def showAccounts(self):
        print('*** Show Accounts ***')
        if len(self.accountsDict) == 0:
            print('no account now.')
            return
        for accountNumber, account in self.accountsDict.items():
            print('number: ', accountNumber)
            account.showAccount()

    def showBank(self):
        print('Hours: ', self.hours)
        print('Address: ', self.address)
        print('Phone: ', self.phone)
        print('We currently have ', len(self.accountsDict),
              ' account(s) open.')
