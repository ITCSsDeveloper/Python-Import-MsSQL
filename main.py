import pyodbc 

# Configs
driver = 'SQL Server'
server = 'localhost\SQLEXPRESS'
db = 'PythonMsSQL'
user = 'sa'
password = 'P@ssw0rd'

# Create Connector
conn = pyodbc.connect('driver={%s};server=%s;database=%s;uid=%s;pwd=%s' % ( driver, server, db, user, password ) )
cursor = conn.cursor()


# CRUD Query
def SelectCustomer():
    cursor.execute('SELECT * FROM customer')
    for row in cursor:
        print(row)

def InsertCustomer():
    pass

def UpdateCustomer():
    pass

def DeleteCustomer():
    pass




# Adv Query
def InsertManyCustomer():
    pass


# EXECUTE Stored return Reuslt


# EXECUTE Stored No Parameter


# EXECUTE SQL Stored + Parameter


SelectCustomer()