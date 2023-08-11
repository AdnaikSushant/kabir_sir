import json, os , json
from connection import connn
import requests

def data(author_id):
    try:
        url = "https://serpapi.com/search.json?engine=google_scholar_author&author_id="+author_id+"&api_key=41835acee14fec19f8813340382d6af658ccd4edb56f35b1b43b4fc841e007c2&num=1000"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        json_obj = (response.json())

        conn=connn
        cursor = connn.cursor()
        for item in json_obj['articles']:
            title=item['title']
            link=item['link']
            citation_id=item['citation_id']
            authors=item['authors']
            try:
                publication=item['publication']
            except:
                publication=""
            cited_link=item['cited_by']['link']
            cited_value=item['cited_by']['value']
            p_year=item['year']
    
        
            try:
        
                cursor.execute('INSERT INTO dbo.gs_data([title],[link],[citation_id],[authors],[publication],[cited_link],[cited_value],[p_year],[author_id]) VALUES (?,?,?,?,?,?,?,?,?)',(title,link,citation_id,authors,publication,cited_link,cited_value,p_year,author_id))

                conn.commit()
            except Exception as e:
                pass
    except Exception as e:
        print(e)
data("CT6kVOYAAAAJ")
