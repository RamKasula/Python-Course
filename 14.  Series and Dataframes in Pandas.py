import pandas as pd

# Load in the following dataset in a Panda Dataframe - http://www.ats.ucla.edu/stat/data/binary.csv
a = pd.read_table('http://www.ats.ucla.edu/stat/data/binary.csv')
print(a)

# Format the dataframe correctly and then print the 1st 5 rows of the dataset
a = pd.read_table('http://www.ats.ucla.edu/stat/data/binary.csv', sep=',') # sep seperates the columns
print(a)

#	Change the column names to
# a.	Enrolled
# b.	Grades
# c.	GPA
# d.	Rank
column_names = ['Enrolled','Grades','GPA','Rank']
b = pd.read_table('http://www.ats.ucla.edu/stat/data/binary.csv', sep=',' , header=None, names=column_names)
c = b.head()
print(c)

#	Print each of the 4 series by themselves
scores = b
scores_Enrolled = b['Enrolled']
print scores_Enrolled
# we can also do this way
print(b['Enrolled'])
print(b['Grades'])
print(b['GPA'])
print(b['Rank'])

# 	Create a new column in the format of Rank - GPA
b['Rank_GPA'] = b['Rank'] + '-' + b['GPA']
print scores
