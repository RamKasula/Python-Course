import pandas as pd
import sqlalchemy


# Adding own column names
user_columns = ['id','name','Abbr','Country','Type','Region Name','Division Name']
states_tbl = pd.read_table('Files/state_table.csv', sep=',', header=None, names=user_columns)

# Loading the data from states_table from python to MySQL
engine = sqlalchemy.create_engine('mysql+mysqldb://root:passw0rd@Localhost/finalproject')
states_tbl.to_sql('states_tbl', engine, if_exists='replace')


dates_tbl = pd.read_excel('Files\Date_dim.xlsx')

engine = sqlalchemy.create_engine('mysql+mysqldb://root:passw0rd@Localhost/finalproject')
dates_tbl.to_sql('dates_tbl', engine, if_exists='replace')


# Loading barget store excel file from Python to MySQL
user_columns = ['Row ID','Order ID','Order Date','Order Priority','Order Quantity','Sales','Discount','Ship Mode','Profit','Unit Price','Shipping Cost','Customer Name','Province','Region','Customer Segment','Product Category','Product Sub-Category','Product Name','Product Container','Product Base Margin','Order Date']
balmart_tbls = pd.read_excel('Files\Store_Balmart.xlsx'.encode('utf-8'),header=None, names=user_columns)

engine = sqlalchemy.create_engine('mysql+mysqldb://root:passw0rd@Localhost/finalproject')

balmart_tbls.to_sql('balmart_tbls', engine,if_exists='replace')

# Loading barget store excel file from Python to MySQL
user_columns = ['Row ID','Order ID','Order Date','Order Priority','Order Quantity','Sales','Discount','Ship Mode','Profit','Unit Price','Shipping Cost','Customer Name','Province','Region','Customer Segment','Product Category','Product Sub-Category','Product Name','Product Container','Product Base Margin','Order Date']
barget_tbl = pd.read_excel('Files\Barget Store.xls', header=None, names=user_columns)

engine = sqlalchemy.create_engine('mysql+mysqldb://root:passw0rd@Localhost/finalproject')
barget_tbl.to_sql('barget_tbl', engine)
