import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

conn = create_connection("cis3368.cejnvvmjqiep.us-east-2.rds.amazonaws.com", "admin", "freg2784", "cis3368fall2021")  #established successful connection with database 

#cursor = conn.cursor(dictionary=True)
#sql = "SELECT * FROM users"
#cursor.execute(sql)
#rows = cursor.fetchall()
#for user in rows:  
    #print(user)

