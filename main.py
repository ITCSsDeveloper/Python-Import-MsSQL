import pyodbc 
import time

# Configs
driver = 'SQL Server'
server = 'localhost\SQLEXPRESS'
db = 'PythonMsSQL'
user = 'sa'
password = 'P@ssw0rd'

# Create Connector
conn = None



try:
    conn =  pyodbc.connect('driver={%s};server=%s;database=%s;uid=%s;pwd=%s' % ( driver, server, db, user, password ) )
except:
    pass

try:
    conn = pyodbc.connect('driver={%s};server=%s;database=%s;trusted_connection=yes' % ( driver, server, db ))  
except:
    pass

if conn == None:
    print('Connection Error.')
    exit()


__start_time = None
__stop_time = None

cursor = conn.cursor()

# CRUD Query
def SelectCustomer():
    cursor.execute('SELECT * FROM customer')
    for row in cursor:
        print(row)

def InsertCustomer(fname, lname, age, gender):
    sql = F"""INSERT INTO Customer (Fname, Lname, Age, Gender)  
              VALUES ('{fname}', '{lname}', '{age}', '{gender}');"""
    cursor.execute(sql)
    cursor.commit()
    pass

def UpdateCustomer(id, fname, lname, age, gender):
    sql = F"""UPDATE Customer
              SET Fname = '{fname}', Lname = '{lname}', Age = '{age}', Gender = '{gender}'
              WHERE Id = '{id}';"""
    cursor.execute(sql)
    cursor.commit()
    pass

def DeleteCustomer(id):
    sql = F"""DELETE Customer WHERE Id = '{id}';""" 
    cursor.execute(sql)
    cursor.commit()
    pass


__data = []
class customerClass: 
    fname : str 
    lname : str
    age : str
    gender : str

def InsertTemp(fname, lname, age, gender):
    temp = customerClass()
    temp.fname = fname
    temp.lname = lname
    temp.age = age,
    temp.gender = gender
    __data.append(temp)



# Can Insert At 1000 rows
def InsertManyCustomer():
    if(len(__data) <= 0):
        return 

    row = 0
    limit = 100
    values = ''
    count_insert = 1

    for item in __data:
        row += 1
        
        if row >= limit :
            print('Insert--->', count_insert)
            count_insert+=1
            values = ''
            row = 0
        else:
            values += F"( '{item.fname}','{item.lname}','{item.age[0]}','{item.gender}' ),"




    # values  = ''
    # for item in __data:
    #     i += 1
    #     print(i)

    #     if i < 1000 : 
    #         total_insert += i
    #         i = 0
    #     else :
    #         print('a')
    #         print(i)

    #     # values += F"( '{item.fname}','{item.lname}','{item.age[0]}','{item.gender}' ),"
    #     # values =  values[0:len(values) -1]
    #     # sql = F""" INSERT INTO Customer (fname, lname, age, gender)
    #     #            VALUES {values}"""
    #     # cursor.execute(sql)
    #     # cursor.commit()


    #     # i = 0
    #     # values = ''
    
    # print('End')

# EXECUTE Stored return Reuslt


# EXECUTE Stored No Parameter


# EXECUTE SQL Stored + Parameter


# SelectCustomer()
# InsertCustomer('F-Name', 'L-Name', '26', 'M')
# UpdateCustomer(11, 'NewFname', 'NewLastName', '30', 'F')
# DeleteCustomer(12)

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    return ("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

for x in range(950):
    InsertTemp(F'FName{x}', F'LName{x}', 22 ,F'M')

__start_time = time.time()
InsertManyCustomer()
__stop_time = time.time()
time_lapsed = time_convert((__stop_time - __start_time))
print('Start', __start_time )
print('Stop', __stop_time )
print('TimeEnd', time_lapsed)

# SelectCustomer()

