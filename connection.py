# import pyodbc
# # SQL Server
# # SQL Server Native Client RDA 11.0
# # ODBC Driver 17 for SQL Server
# # MySQL ODBC 8.0 ANSI Driver
# # MySQL ODBC 8.0 Unicode Driver
# server = 'localhost'
# database = 'gs_data'
# username = 'root'
# password = ''
# # root@localhost:3306
# try:
    
#     connn=pyodbc.connect('SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
#     print(connn)
# except Exception as e:
#     print("Error in connections: " ,e)
import mysql.connector

server = 'localhost'
database = 'gs_data'
username = 'root'
password = 'root'

try:
    connn = mysql.connector.connect(
        host=server,
        database=database,
        user=username,
        password=password
    )
    print("Connection successful!")
except Exception as e:
    print("Error in connection:", e)

