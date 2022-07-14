class Atm:

    def __init__(self):
        self.pin = None
        self.balance = 0
        self.menu()

    def menu(self):
        print('\n 1. Create Pin \n 2. Deposit \n 3. Withdraw \n 4. Check Balance \n 5. Exit')
        self.user_input = input('Enter the choice to proceed -- ')
        if self.user_input == '1':
            self.create_pin()
        elif self.user_input == '2':
            self.deposit()
        elif self.user_input == '3':
            self.withdraw()
        elif self.user_input == '4':
            self.check_balance()
        elif self.user_input == '5':
            print('Thank you')    
        else:
            self.menu()
    
    def create_pin(self):
        self.pin = int(input('enter the pin - '))
        print('set successfully!!!')
        self.menu()
    
    def deposit(self):
        self.temp = int(input('Enter the pin -- '))
        if self.temp == self.pin:
            self.amount = int(input('Enter the amount -- '))
            self.balance += self.amount
            print('Successfully deposited')
        else:
            print('Invalid Pin, enter again -- ')
        self.menu()

    def withdraw(self):
        self.temp = int(input('Enter the pin -- '))
        if self.temp == self.pin:
            self.amount = int(input('Enter the withdraw amount -- '))
            if self.balance >= self.amount:
                self.balance -= self.amount
                print('successfull')
            else:
                print('Insufficient Funds')
        else:
            print('invalid pin , Enter again - ')
        self.menu()

    def check_balance(self):
        self.temp = int(input('Enter the pin -- '))
        if self.temp == self.pin:
            print('The balance is', format(self.balance, '.2f'))
        else:
            print('invalid pin , Enter again - ')
        self.menu()

