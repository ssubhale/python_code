# Implement bank application in OOP

# Note:
'''
1. Instance variables : Name, Amount, Address, Account
2. Instance methods   : CreateAccount(), DisplayAccInfo()
3. Class variables    : Bank_Name, ROI_ON_FD
4. Class method       : DisplayBankInfo()
5. Static method      : DisplayKYCInfo()
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
    def displayBankInfo(cls):
        print("Welcome to banking console")
        print(f"Name of our bank is : {cls.Bank_Name}")
        print(f"Rate of interest we offer on fixed deposite is : {cls.ROI_On_FD}%")

    @staticmethod
    def displayKYCInfo():
        print("------ Please consider bellow KYC information ------\n"
            "According to the rules of Government of India, You have to submit bellow document\n"
            "1. Clear and recent passport size photo\n"
            "2. Photo of Aadhar Card\n"
            "3. Photo of PanCard"
            )

    def Deposit(self,value):
        self.Amount += value

    def Withdraw(self,value):
        self.Amount -= value

    def CheckBal(self):
        print("Your account balance is : ",self.Amount)


def main():
    print("Application for creating bank account")

    Bank_Account.displayKYCInfo()
    Bank_Account.displayBankInfo
    user1 = Bank_Account()

    print("---------- Enter the details of account holder ----------")
    user1.CreateAccount()
    user1.DisplayAccInfo()

    user1.Deposit(int(input("\nEnter amount for deposite : ")))
    user1.CheckBal()

    user1.Withdraw(int(input("\nEnter amount for withdraw : ")))
    user1.CheckBal()

if __name__ =="__main__":
    main()