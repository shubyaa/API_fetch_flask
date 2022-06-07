import mysql.connector as connect

conn = connect.connect(
    host="localhost",
    user="root",
    passwd="8451841454aA@",
    auth_plugin="caching_sha2_password"
)

cursor = conn.cursor()

# to create the database
# cursor.execute("CREATE DATABASE database_interactions")
cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)