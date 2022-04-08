# Account class
# Errors indicated by raise statements

# Define a custom exception


class AbortTransaction(Exception):
    '''raise the exception to abort a bank transation'''
    pass


class Account():

    def __init__(self, name, balance, password):

        self.name = name
        self.balance = self.validateAmount(balance)
        self.password = password

    def validateAmount(self, amount):
        '''ensure that the amount is an integer and positive'''
        try:
            amount = int(amount)
        except ValueError:
            raise AbortTransaction('Amount must be an integer')

        if amount <= 0:
            raise AbortTransaction('Amount must be positive')

        return amount

    def checkPasswordMatch(self, password):
        if self.password != password:
            raise AbortTransaction('Incorrect password for this account')

    def deposit(self, amountToDeposit):
        amountToDeposit = self.validateAmount(amount=amountToDeposit)
        self.balance += amountToDeposit
        return self.balance

    def getBalance(self):
        return self.balance

    def withdraw(self, amountToWithdraw):
        amountToWithdraw = self.validateAmount(amount=amountToWithdraw)
        if amountToWithdraw > self.balance:
            raise AbortTransaction('You can\'t withdraw more than you have')
        self.balance -= amountToWithdraw
        return self.balance

    # Added for debugging
    def showAccount(self):
        print('     Name: ', self.name)
        print('     Balance: ', self.balance)
        print('     Password: ', self.password)
