# Implement bank application in OOP

# Note:
'''
1. Instance variables : Name, Amount, Address, Account
2. Instance methods   : CreateAccount(), DisplayAccInfo()
3. class variables    : Bank_Name, ROI_ON_FD
4. Class method       : DisplayBankInfo()
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

    @classmethod
    def DisplayBankInfo(cls):
        print("---------- Welcome to banking console ----------")
        print("Name of our bank is : ",cls.Bank_Name)
        print("Rate of interest we offer on fixed deposite is : ",cls.ROI_ON_FD)


def main():
    print("Application for creating bank account")

    user1 = Bank_Account()
    user1.DisplayBankInfo()

    print("---------- Creating first account ----------")
    user1.CreateAccount()
    user1.DisplayAccInfo()

if __name__ =="__main__":
    main()