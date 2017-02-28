# Dictionaries in Python

#2.	Create 2 Dictionaries
#1.	Cars Add 5 entries.  Intentionally spell one of your Car Models incorrectly.
#a.	Key = Make
#b.	Value = Model
#2.	Trucks Add 5 entries
#a.	Key = Make
#b.	Value = Model
#3.	Cars and Trucks (Empty)

Cars = {'Jaguar':'Xe','Audi':'A4','Honda':'Civic','Hyundai':'Elantra','Toyota':'Camre'}
Trucks = {'Dodge':'Ram','Ford':'Ranger','Chevy':'Colarado','Nissan':'Titan','Toyota':'Tundra'}
Cars.clear() #To empty the Cars Dictionary
print Cars
Trucks.clear() # To empty the the Trucks Dictionary
print Trucks

#3.	Copy the Cars and Trucks dictionaries into the Cars and Trucks dictionary.
Cars = {'Jaguar':'Xe','Audi':'A4','Honda':'Civic','Hyundai':'Elantra','Toyota':'Camre'}
cars = Cars.copy() #Copying from one dictioanry to the other Dictionary
print cars
Trucks = {'Dodge':'Ram','Ford':'Ranger','Chevy':'Colarado','Nissan':'Titan','Toyota':'Tundra'}
trucks = Trucks.copy() #copying from Trucks to trucks Dictionary
print trucks

#4.	Do a search on a Make you know is not in the Cars dictionary.  (Display the FALSE results)
print 'Nissan' in Cars #checking wether the value exist in dictionary

#5.	Delete 3 entries from the Cars and 2 entriese from the Trucks dictionary
del cars["Toyota"] #deleting values from dictionary
del cars['Hyundai']
del cars['Honda']
print cars

del trucks['Dodge']
del trucks['Ford']
print trucks

#6.	Create a For Loop to display all of the Cars and Trucks from the 2 dictionaries.
#	For Every Car or Truck, you will display I like this car/truck:  <<Car/Truck>>
for (keys,values),(keys2,values2) in zip(cars.items(),trucks.items()) : #zip is used to iterate over two lists or dictionaries
    print "I like this %s,%s" %(keys,values)
    print "I like this %s,%s" %(keys2,values2)
