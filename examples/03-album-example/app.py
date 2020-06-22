import pymysql
import os
from dotenv import load_dotenv

#load in the environment variables
load_dotenv()

#create the database connection
conn = pymysql.connect(host="localhost",
                        user=os.environ.get("DB_USER"),
                        password=os.environ.get("DB_PASSWORD"),
                        database="Chinook")

#Create the cursor
cursor = conn.cursor(pymysql.cursors.DictCursor)

#Define the sql statement
track_name=input("Please enter a track name: ")

sql = f"""
select * from Track
where Name like "%{track_name}%"
limit 10
"""

#Execute the statement
cursor.execute(sql)

#Output the results
for each_result in cursor:
    print("Track: ", each_result['Name'])
    print("Composed by: ", each_result['Composer'])
    print()