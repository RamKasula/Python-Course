#2.	Create and print a list of 10 of your favorite foods (FoodList)
FoodList=['pizza','Sandwich','Poori','GulabJam','Roti','Rice','Chicken','Burger','Taco','Fries']
print FoodList

#3.	Create and print a list of 10 of your favorite cars (CarList)
CarList =['Audi', 'Jaguar', 'BMW', 'Benz', 'Lamborghini', 'Ferrari', 'Porsche', 'Toyota', 'Nissan', 'Honda']
print CarList

#4.	Add 3 entries to both list
FoodList.extend(['Salad', 'ChickenPizza', 'Nuggets'])
print FoodList
CarList.extend(['Hyundai','Mahindra','Coevette'])
print CarList

#5.	Create a For Loop that loops through the FoodList and prints I love eating <<Food>>
#   for each member in your list.
for i in FoodList:
    print "I love eating %s" %i
#6.	Create a For Loop that loops through the CarList and prints I love driving <<Car>>
#   for each member in your list.
for i in CarList:
    print "I love driving %s" %i

#7.	Create a variable and set it equal to a range of integers starting at 150 and goes to 200 by 5
var_range = range(150,200,5)
print var_range

#8.	Create a For Loop for the same range created in #7.  Just Added: <<Number>> to the list
for i in var_range:
    print "Just Added %d to the list" %i

#9.	Create a WHILE Loop that loops through every value in your CarList
#a.	Print I cant afford a <<Car>> just yet
#b.	Delete that car from the list after the print statement
#c.	Once the While Loop completes, all the cars should be deleted from the list.

i = 0
while i < len(CarList):
    car = CarList[i]
    print "I can't afford a just yet",car
    CarList.remove(CarList[0])
    i = 0 + 1
    print CarList
