
import re
import pyodbc
def selected_rec(data):
    columns = data
    try:
        conn=pyodbc.connect(Driver="SQL Server",
                            host="DESKTOP-DFF341V\SQLEXPRESS",
                            Database = "master",
                            Trusted_Connection="yes")

        cursor = conn.cursor()
    except Exception as e:
        print(e)
    query = f'SELECT {",".join(columns)} FROM gs_data;'
    try:
        result = list(cursor.execute(query))
        responseArray =[]
        for row in result:

            paramsDict = {}
            for i in range(0, len(columns)):
                try:
                    paramsDict[columns[i]] = row[i]
                except:
                    paramsDict[columns[i]] = 0

            responseArray.append(paramsDict)
           
    except Exception as e:
        print(e)  
    conn.close()
    return responseArray

