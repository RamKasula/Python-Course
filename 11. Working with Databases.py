# 	Connect to your MySQL Server / adventureworks database
import mysql.connector

db = mysql.connector.connect(user = 'root', password = 'passw0rd', host = 'Localhost', database = 'adventureworks')
mycursor = db.cursor()

#	Find total Sales by Credit Card Type
mycursor.execute(" SELECT      CardType, SUM(a.TotalDue) AS TotalSales \
                    FROM        salesorderheader a\
                    INNER JOIN  creditcard b \
                    ON          a.CreditCardID = b.CreditCardID \
                    GROUP BY    CardType;")
print(mycursor.fetchall())

#  Find total Sales by Product
mycursor.execute(" SELECT        p.Name, SUM(soh.TotalDue) AS TotalSales \
                   FROM          salesorderheader soh \
                   INNER JOIN    salesorderdetail sod \
                   ON            soh.SalesOrderID = sod.SalesOrderID \
                   INNER JOIN    product p \
                   ON            sod.productID = p.productID \
                   GROUP BY      p.Name;")
print(mycursor.fetchall())

# Find total Sales by Ship State
mycursor.execute(" SELECT      sp.Name, SUM(soh.TotalDue) AS TotalSales \
                   FROM        salesorderheader soh \
                   INNER JOIN  salesterritory st  \
                   ON          soh.territoryID = st.territoryID \
                   INNER JOIN  stateprovince sp \
                   ON          sp.territoryID = st.territoryID \
                   GROUP  BY   sp.Name;")
print(mycursor.fetchall())

#   Find total Sales by Territory Group
mycursor.execute(" SELECT      st.Group, SUM(soh.TotalDue) AS TotalSales \
                   FROM        salesorderheader soh \
                   INNER JOIN  salesterritory st  \
                   ON          soh.territoryID = st.territoryID \
                   GROUP  BY   st.Group;")
print(mycursor.fetchall())

#  Find Total Sales by Ship Method
mycursor.execute(" SELECT      sm.Name, SUM(soh.TotalDue) AS TotalSales \
                   FROM        salesorderheader soh \
                   INNER JOIN  shipmethod sm  \
                   ON          soh.shipmethodID = sm.shipmethodID \
                   GROUP  BY   sm.Name;")
print(mycursor.fetchall())

#  Find Total Sales by Product Subcategory.
mycursor.execute(" SELECT        psc.Name, SUM(soh.TotalDue) AS TotalSales \
                   FROM          salesorderheader soh \
                   INNER JOIN    salesorderdetail sod \
                   ON            soh.SalesOrderID = sod.SalesOrderID \
                   INNER JOIN    product p \
                   ON            sod.productID = p.productID \
                   INNER JOIN    productsubcategory psc \
                   ON            psc.productsubcategoryID = p.productsubcategoryID \
                   GROUP BY      psc.Name;")
print(mycursor.fetchall())
