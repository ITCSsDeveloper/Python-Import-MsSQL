ในเว็บ Ms แนะนำว่ามี lib driver อยู่ 2 ตัว 
 - pyodbc
 - pymssql

แต่จากการหาข้อมูลพบว่า ส่วนใหญ่แนะนำให้ใช้ Pyodbc เพราะ มีการพัฒนาเรื่อยๆ และ ความนิยมเยอะกว่า pymssql 
pyodbc มีฟีเจอร์การใช้งานครอบคุมมากกว่า และ เชื่อมต่อได้หลาย Database
pyodbc มี dependecy น้อยกว่า pymssql 


Note Vocabulary
** Open Database Connectivity (ODBC) (Potocol)
** FreeTDS is a set of libraries for Unix and Linux that allows your programs to natively talk to Microsoft SQL Server and Sybase databases. 



Python SQL Driver
 - Python SQL driver - pyodbc  (2000+ stars on github)
 - Github : https://github.com/mkleehammer/pyodbc/
 - pyodbc is an open source Python module that makes accessing ODBC databases simple. It implements the DB API 2.0 specification but is packed with even more Pythonic convenience.
 - Imprement with C++
 - Multi Database Access ( mssql, mysql, postgres, excel, access )

 - Python SQL driver - pymssql (500+ stars on github)
 - Github : https://github.com/pymssql/pymssql
 - A simple database interface for Python that builds on top of FreeTDS to provide a Python DB-API (PEP-249) interface to Microsoft SQL Server.
 - Imprement with cPython
 - for MS Sql Server
 


Example Connections
# using keywords for SQL Server authentication
self.db = pyodbc.connect(driver=driver, server=server, database=db,
                         user=user, password=password)

# using keywords for Windows authentication
self.db = pyodbc.connect(driver=driver, server=server, database=db,
                         trusted_connection='yes')   


Ref : 
https://www.sqlshack.com/performing-crud-operations-with-a-python-sql-library-for-sql-server/