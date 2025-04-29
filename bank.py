import os
class BankAccount:
    globelaccount = 0
    
    def __init__(self, name:str, email:str, balance:int):
        BankAccount.globelaccount += 1
        self.name = name
        self.email = email
        self.accountnumber = BankAccount.globelaccount
        self.balance = balance
    
    def deposit(self, money):
        if money > 0:
            self.balance = int(self.balance) + money
            print("deposited")
        else:
            print("You must deposit an amount of money greater than 0")
    
    def withdraw(self, money):
        if money<=0:
           print("You must withdraw an amount of money greater than 0")
        elif money <= self.balance:
            self.balance = int(self.balance) + money
            print("withdrawn")
        else:
            print("The amount of money you are trying to withdraw is greater than your balance, you have withdrawn the entirety of your balance")
            self.balance = 0

    def seebalance(self):
        print("Balance: $",self.balance)
    
    def seedetails(self):
        print("Name: ",self.name)
        print("Email: ",self.email)
        print("Account Number: ",self.accountnumber)
        print("Balance: $",self.balance)
    
    def save(self, name, email, accountnumber, balance):
        File = open(name, "w")
        File.write(name)
        File.write("\n")
        File.write(email)
        File.write("\n")
        File.write(accountnumber)
        File.write("\n")
        File.write(str(balance))
        File.write("\n")

    def save(self):
        File = open("People/" + self.name, "w")
        File.write(self.name)
        File.write("\n")
        File.write(self.email)
        File.write("\n")
        File.write(str(self.accountnumber))
        File.write("\n")
        File.write(str(self.balance))
        File.write("\n")
    
    def update(self, name1, emal, anum):
        File = open("People/" + name1, "w")
        File.write(name1)
        File.write("\n")
        File.write(email)
        File.write("\n")
        File.write(str(anum))
        File.write("\n")
        File.write(str(self.balance))
        File.write("\n")

    def setaccountnumber(self):   
        directory = "People"
        count = 0    
        for i in os.listdir(directory):
            with open(os.path.join(directory, i)) as f:
                #print(f.read())
                count += 1
        self.accountnumber = count + 1

def money(self):
    money = input("Type withdraw if you want to withdraw. Type deposit if you want to deposit. ")
    if money == "withdraw":
        withdraw = input("How much money do you want to withdraw? ")
        self.withdraw(int(withdraw))
        print("Your new balance is" , self.balance)
    if money == "deposit":
        deposit = input("How much money do you want to deposit? ")
        self.deposit(int(deposit))
        print("Your new balance is" , self.balance)

def getaccountbal(name):
    File = open("People/" + name, "r")
    lines = File.readlines()
    return lines[3]

def getaccountnum(name):
    File = open("People/" + name, "r")
    lines = File.readlines()
    return lines[2]

def getaccountemail(name):
    File = open("People/" + name, "r")
    lines = File.readlines()
    return lines[1]

def confirmaccount(name, email, accountnum):
    File = open("People/" + name, "r")
    lines = File.readlines()
    if (lines[1] == (email + "\n")) and (lines[2] == (accountnum + "\n")):
        print("Account found")
    else:
        print("Incorrect account details")
        quit()

login = input("If you want to log in, type log in. If you want to sign up, type sign up. ")
if login == "log in":
    name=input("What is your name? ")
    email=input("What is your email? ")
    accountnum=input("What is your account number? ")
    confirmaccount(name, email, accountnum)
    temp_account = BankAccount("TEMP", "TEMP", getaccountbal(name))
    money(temp_account)
    temp_account.update(name, email, accountnum)

if login == "sign up":
    name=input("What is your name? ")
    email=input("What is your email? ")
    User_account = BankAccount(name, email, 0)
    User_account.setaccountnumber()
    User_account.save()
    User_account.seedetails()
    money(User_account)

