import pandas as pd

# Loading the file into pandas dataframe
consumer_complaints = pd.read_csv('Files/Consumer_Complaints.csv')
print(consumer_complaints)

#  Retrieve the 1st 5 rows of the dataset
print(consumer_complaints.head())

# 	Delete the following columns and then display the 1st 5 rows in the new dataset
# a.	Consumer complaint narrative
# b.	Company public response
# c.	Consumer consent provided
# d.	Consumer disputed?
# e.	Complaint ID
# f.	Tags
# g.	Issue
consumer_complaints.drop(['Consumer complaint narrative','Company public response','Consumer consent provided?','Consumer disputed?','Complaint ID','Tags','Issue'], axis=1, inplace=True)
# print(consumer_complaints.head())

# How many rows and columns are in the dataset.
print(consumer_complaints.shape)

# Delete rows 0 to 1000.
consumer_complaints.drop(range(0,1001), axis=0, inplace=True)

# How many rows and columns are in the dataset.
print(consumer_complaints.shape)

# Sort the dataframe by Date Received descending  Print Dataframe
print(consumer_complaints.head().sort_values('Date received', ascending=False)) # sort ascending is default

# Find the number of disputes by Company
consumer_complaints = pd.read_csv('Files/Consumer_Complaints.csv')
print(consumer_complaints.groupby('Company')['Consumer disputed?'].count())

# Find the number of disputes by State
print(consumer_complaints.groupby('State')['Consumer disputed?'].count())

# Find the number of disputes by DateReceived Year, Month descending
# lets convert the column to a pandas datetime formatted

consumer_complaints['Date received'] = pd.to_datetime(consumer_complaints['Date received'])

print(consumer_complaints.groupby('Date received')['Consumer disputed?'].count()).sort_values(['Date received']['dt']['year'],'Date received']['dt']['month'], ascending=False)

print(consumer_complaints.sort_values(['Date received']).groupby('Date received')['Consumer disputed?']).count()
