import mysql.connector
import time

# MYSQL Database Connection
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "YOUR_PASSWORD",
    database = "YOUR DB NAME"
)
cursor = connection.cursor()

def fetch_last_data():
    cursor.execute("SELECT * FROM your_table ORDER BY id DESC LIMIT 5")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# REAL TIME DATABASE MONITOR        
while True:
    fetch_last_data()
    print("waiting for the REFRESH...")
    time.sleep(10)