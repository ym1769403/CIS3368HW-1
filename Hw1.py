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


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


conn = create_connection("cis3368.cejnvvmjqiep.us-east-2.rds.amazonaws.com", "admin", "freg2784", "cis3368fall2021") 
#established successful connection with database. conn is the connection object

# use data and how to sort records(find sorting algorithm and cite/explain) for this assignment 
#this inserts an entry to table 
#query = "INSERT INTO shopcart (firstname, lastname) VALUES ('Thomas','Edison')" 
#execute_query(conn, query)  

#cursor = conn.cursor(dictionary=True)
#sql = "SELECT * FROM users"
#cursor.execute(sql)
#rows = cursor.fetchall()
#for user in rows:  
    #print(user)





#create menu
def menu():
    print('a - Add item')
    print('d - Remove item')
    print('u - Update item details')
    print('r1 - Output all items in alphabetical order')
    print('r2- Output all items by sorted by quantity (ascending)')
    print('q - Quit') 

menu()
option = input('Enter your option')
 #then loop next? 






