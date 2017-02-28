# Working with Dates

#	Import datetime and time modules
import datetime
import time

# 	Print todays date
print datetime.date.today() #we can print directly

today = datetime.date.today() # we can print by assigning it to the variable
print "Today's date is ",today

#	Subtract 3 weeks / 2 days  / 3 hours from todays date
today = datetime.datetime.today()
threeWk = datetime.timedelta(weeks=3) #timnedelta is used to sum or substract the number of days and time
twodays = datetime.timedelta(days=2)
threehours = datetime.timedelta(hours=3)

print today - threeWk - twodays - threehours

# 	Extract each from todays date
#a.	Year
#b.	Month
#c.	Day
#d.	Hour
#e.	Minute
#f.	Seconds
today = datetime.datetime.today()
print today
print today.year
print today.month
print today.day
print today.hour
print today.minute
print today.second

#	Then format the date (YY,MM,DD HH,MM,SS)
format = '%Y %b %a %H:%M:%S' #Y=Year,b=Month,a=Day,H=Hour,M=Minute,S=second
DateFormat = today.strftime(format) #strftime converts the time to the given string format.
print DateFormat
