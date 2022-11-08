class bank:
    def start(self):
        self.number=int(input("Enter ac. number: "))
        self.name=input("Enter name: ")
        self.balance=int(input("Enter balance: "))
    def display(self1):
        print("Number: ",self1.number)
        print("Name: ",self1.name)
        print("Total Balance: ",self1.balance)
    
    
    def deposit(self2):
        self2.balance=self2.balance+int(input("Enter amount to deposit: "))
        print("Amount after deposit: ",self2.balance)
    def withdraw(self3):
        self3.balance=self3.balance-int(input("Enter amount to withdraw: "))
        print("Amount after withdrawal: ",self3.balance)

obj1=bank()
obj1.start()
obj1.deposit()
obj1.withdraw()
obj1.display()