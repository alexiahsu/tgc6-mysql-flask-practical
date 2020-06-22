from data import get_conn, get_cursor
import os

conn = get_conn("localhost",
                os.environ.get("DB_USER"),
                os.environ.get("DB_PASSWORD"),
                "Chinook"
                )
cursor = get_cursor(conn)

while True:
    print("Select what to search by: ")
    print("1. Artist Name")
    print("2. Composer Name")
    print("3. Quit")

    choice = input("Enter your choice: ")
    sql = ""

    if choice == "1":
        track_name=input("Please enter a track name: ")

        sql = f"""
        select * from Track
        where Name like "%{track_name}%"
        limit 10
        """
    elif choice =="2":
        composer_name=input("Please enter the composer name: ")

        sql = f"""
        select * from Track where composer like "%{composer_name}%"
        """

    elif choice == "3":
        break

    cursor.execute(sql)

    print("Search results")
    for each_result in cursor:
        print("Track name: ", each_result["Name"])
        print("Composers: ", each_result["Composer"])

