
import re
from connection import connn
def selected_rec(data):
    columns = data
    try:
              
        conn =connn
        cursor = conn.cursor()
    except Exception as e:
        print("*********************",e)
    query = f'SELECT {",".join(columns)} FROM google_scholar;'
    try:
        cursor.execute(query)
        result = list(cursor.fetchall())
        responseArray =[]
        for row in result:
            print(row)
            paramsDict = {}
            for i in range(0, len(columns)):
                try:
                    paramsDict[columns[i]] = row[i]
                except:
                    paramsDict[columns[i]] = 0

            responseArray.append(paramsDict)
           
    except Exception as e:
        print(e) 
    finally:     
        conn.close()
        return responseArray

# selected_rec(['title', 'p_year', 'authors'])