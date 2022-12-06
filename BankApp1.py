# Mini bank application by using global variable

balance = 2000

def Deposite(damt):
    global balance
    balance += damt

def Withdraw(wamt):
    global balance
    balance -= wamt

def Balance_Check():
    print("Available balance is : ",balance)

Deposite(int(input("Enter deposite amount : ")))

Balance_Check()

Withdraw(int(input("Enter withdraw amount : ")))

Balance_Check()