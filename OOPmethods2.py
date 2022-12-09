# Implement bank application in OOP

# Note:
'''
1. Instance variables : Name, Amount, Address, Account
2. Instance methods   : CreateAccount(), DisplayAccInfo()
3. Class variables    : Bank_Name, ROI_ON_FD
'''

class Bank_Account:

    Bank_Name = "MICDC pvt ltd"
    ROI_ON_FD = 6.7

    def __init__(self):
        self.Name = ""
        self.Amount = 0
        self.Address = ""
        self.AccountNo = 0

    def CreateAccount(self):
        self.Name = input("Enter your name : ")
        self.AccountNo = int(input("Enter account number : "))
        self.Amount = int(input("Enter your initial amount : "))
        self.Address = input("Enter your address : ")

    def DisplayAccInfo(self):
        print("------ Your Account information is as bellow -------")
        print("Name of Account holder = ",self.Name)
        print("Account number = ",self.AccountNo)
        print("Current amount in Account = ",self.Amount)
        print("Address of Account holder = ",self.Address)

def main():
    print("Application for creating bank account")

    print("Name of bank : ",Bank_Account.Bank_Name)
    print("Rate of Inteest on Fixed Deposite : ",Bank_Account.ROI_ON_FD)

    user1 = Bank_Account()
    user2 = Bank_Account()

    print("---------- Creating first account ----------")
    user1.CreateAccount()
    print("---------- Creating first account ----------")
    user2.CreateAccount()

    user1.DisplayAccInfo()
    user2.DisplayAccInfo()

if __name__ =="__main__":
    main()