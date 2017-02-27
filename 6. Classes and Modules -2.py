#Input the Script5LabMod1.py Module to the Script5Lab.py file.
import Script5LabMod1

#Create 3 objects and pass the CheckingAccountBalance Class to both objects
Customer1 = Script5LabMod1.CheckingAccountBalance()
Customer1.deposit('Ram')
Customer1.withdrawal('Ram')

Customer2 = Script5LabMod1.CheckingAccountBalance()
Customer2.deposit('John')
Customer2.withdrawal('John')

Customer3 = Script5LabMod1.CheckingAccountBalance()
Customer3.deposit('kyle')
Customer3.withdrawal('kyle')

#Call the Methods 10 times between the 3 objects
Customer1 = Script5LabMod1.CheckingAccountBalance()
Customer1.deposit('Ram')
Customer1.withdrawal('Ram')
Customer1.deposit('Ram')
Customer2.deposit('John')
Customer3.withdrawal('kyle')
Customer3.deposit('kyle')
Customer2.deposit('John')
Customer2.withdrawal('John')
Customer1.deposit('kyle')
Customer1.deposit('Ram')
