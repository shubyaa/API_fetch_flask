import mysql.connector as connect
from dotenv import load_dotenv
import os

load_dotenv()

def create_database():

    conn = connect.connect(
        host="localhost",
        user="root",
        passwd=os.getenv("passwd"),
        auth_plugin="caching_sha2_password"
    )

    cursor = conn.cursor()

    # to create the database
    cursor.execute("CREATE DATABASE {0}".format(os.getenv("passwd")))
    cursor.execute("SHOW DATABASES")
    for db in cursor:
        print(db)


# Call this to execute the above operation
# create_database()