import pyodbc

connection = pyodbc.connect("Driver={SQL Server};"
                      "Server=.;"
                      "Database=SHP4;"
                      "Trusted_Connection=yes;")
cursor = connection.cursor()
cursor.execute('SELECT * FROM SHP_Product')

for i in cursor:
    print(i)
