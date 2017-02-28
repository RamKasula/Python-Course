import os # os is the built in module in python

#	Create a new folder in your working directory called Script9LabAssignment
os.chdir('C:\Colaberry1\PythonClass\ExternalScripts\Files\Script9LabAssignment') #chdir is used to change the directory
print os.getcwd() # getcwd is used to get the current working directory

filepath = open('C:\Colaberry1\PythonClass\ExternalScripts\Files\Script9LabAssignment\Assignment.txt','w') # w is the parameter used to write in textfile
filepath.write(''' This is my assignment for Lab 9.
I know that it is easy to create textfiles in Python
I just need to relax and follow the yellow brick road''')
filepath.close()

#	Create the following Excel Spreadsheet using Python.

from xlwt import Workbook, Formula, easyxf # xlwt is built in module in python used to work with excelfiles.
wb = Workbook()
sheet1 = wb.add_sheet('Sheet1') #add_sheet is used to add anew sheet in the excel file.
style1 = easyxf('pattern : pattern solid, fore_color yellow;') #easyfx is used to style cells in excel.
sheet1.write(0,0,'Column1') # to write the data in format of row, column, value.
sheet1.write(0,1,'Column2')
sheet1.write(0,2,'Column3')
wb.save('xlwt Assignment.xls')
# For Column1 values
for i in xrange(1,11):
    sheet1.write(i,0,i)
sheet1.write(11,0,Formula('SUM(A2:A11)'),style1) #Formula is used to write fomula in excel.
wb.save('xlwt Assignment.xls')
# For column2 values
for i,j in zip(xrange(1,11),xrange( 100,200,10)):
    sheet1.write(i,1,j)
sheet1.write(11,1,Formula('SUM(B2:B11)'),style1)
wb.save('xlwt Assignment.xls') # save is used to save the excel file.
# For column3 values
for i,j in zip(xrange(1,11),xrange(1500,15001,1500)):
    sheet1.write(i,2,j)
sheet1.write(11,2,Formula('SUM(C2:C11)'),style1)
wb.save('xlwt Assignment.xls')
