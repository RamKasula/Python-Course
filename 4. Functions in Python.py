#Lab of Functions in python

#2.	Create a function called NonYaBusiness that accepts 0 parameters and
#    returns the statement None of your business
def NonYaBusiness():
    print  "None of your business"

NonYaBusiness()

#3.	Create a List of Names and add 10 names to the list
#a.	Create a function that accepts a name
#b.	In the function, add the input parameter name to the Names list
#c.	Print the full list as the last step in the function
#d.	Add 5 more names to the list using the function
#e.	Document the function
#f.	Retrieve documentation from function
list = ['Ram','Anand','Ashok','Sai','Ali','Alex','Ron','Sairam','Balram','Abhiram']
print list

def NameFunction(name):
    '''
    Adding input parameter name to the list
    Print list which incules the input parameter
    Adding 5 more names to the list
    Print the whole list
    '''
    list.append(name);
    print list
    list.extend(['Varma','John','Micah','Mike','Kyle'])
    print list

NameFunction('Raghu')

print NameFunction.__doc__
