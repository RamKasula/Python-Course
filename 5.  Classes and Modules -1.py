#2.	In Script5LabMod1.py you wil
#a.	Create a class called CheckingAccountBalance.  Create an initial variable (StartingAmount) and
#set it equal to $1k.  Within the Class you will create 2 Methods
#i.	Method1 (deposit) will accept one value
#1.	User will be asked how much they would like to deposit
#2.	Once user enters amount, that amount is added to their Balance
#3.	Print the new balance
#ii.	Method2 (withdrawal) will accept one value
#1.	User will be asked how much they would like to withdraw
#2.	Once user enters amount, that amount is deducted from their Balance
#3.	Print the new balance


class CheckingAccountBalance:
    startingAmount = 1000 #Global Variable to the class
    def deposit(self,name):
        self.name = name
        value = raw_input('How much would you like to deposit: ') #Assigning raw input value
        self.value = value
        self.startingAmount += int(self.value) #Adding raw input value to the StartingAmount balance
        print ("Hi %s,Your new balance is %s") %(self.name,self.startingAmount)

    def withdrawal(self,name):
        self.name = name
        value = raw_input('How much would you like to withdraw: ') #Assigning raw input value
        self.value = value
        self.startingAmount -= int(self.value) #Subtracting the raw inpt value from the startingAmount
        print("Hi %s, Your new balance is %s") %(self.name,self.startingAmount)
