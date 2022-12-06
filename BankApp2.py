#  Bank application without using global keyword

balance = 2000

def Deposite(balance, damt):
    balance += damt
    return balance

def Withdraw(balance,wamt):
    balance -= wamt
    return balance

def Balance_Check():
    print("Available balance is : ",balance)

balance = Deposite(balance,int(input("Enter deposite amount : ")))

Balance_Check()

balance = Withdraw(balance, int(input("Enter withdraw amount : ")))

Balance_Check()