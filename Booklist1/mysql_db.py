import mysql.connector

con = mysql.connector.connect(
    user="", 
    password = "", 
    host="", 
    database = ""
)
cursor = con.cursor()
query = cursor.execute("SELECT * FROM データベース WHERE Expression = )
results = cursor.fetchall()
if results:
    for result in results:
        print(result[1])
else:
    print("We couldn't find any results about that.")