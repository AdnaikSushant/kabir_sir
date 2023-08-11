import pyodbc
connn=pyodbc.connect(Driver="SQL Server",
                    host="DESKTOP-DFF341V\SQLEXPRESS",
                    Database = "master",
                    Trusted_Connection="yes")