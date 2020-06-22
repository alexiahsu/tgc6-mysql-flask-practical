import pymysql
import os

from dotenv import load_dotenv
load_dotenv()

conn = pymysql.connect(host='localhost',
                        user=os.environ.get('DB_USER'),
                        password=os.environ.get('DB_PASSWORD'),
                        database="Chinook")

cursor = conn.cursor(pymysql.cursors.DictCursor)

sql = """
select * from Album join Artist on Album.ArtistId=Artist.ArtistId 
Limit 10
"""

cursor.execute(sql)

for each_result in cursor:
    print("Album:", each_result["Title"])
    print("")

