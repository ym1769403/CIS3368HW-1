from re import T
import mysql.connector
from mysql.connector import Error
import datetime
from datetime import date 
today = date.today()
#https://stackabuse.com/how-to-format-dates-in-python/ 

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


conn = create_connection("cis3368.cejnvvmjqiep.us-east-2.rds.amazonaws.com", "admin", "freg2784", "cis3368fall2021")  #established successful connection with database conn is the connection object
 
cursor = conn.cursor(dictionary=True)
sql = "SELECT * FROM shoppinglist"
cursor.execute(sql)
rows = cursor.fetchall()
for items in rows:
    print(items)


#def slist():
    #cursor = conn.cursor(dictionary=True)
    #sql = "SELECT * FROM shoppinglist"
    #cursor.execute(sql)
    #rows = cursor.fetchall()
    #for items in rows:  
         #print(items)  

#slist()     # this returns the whole table made

#create the menu
def menu():
    print('a - Add item')
    print('d - Remove item')
    print('u - Update item details')
    print('r1 - Output all items in alphabetical order')
    print('r2- Output all items by sorted by quantity (ascending)')
    print('q - Quit') 
    option = input('Enter your option')
    while True:
        if option == 'a':
            add_id = input('Enter id')
            add_item_description = input('Enter item description')
            add_quantity =  input('Enter item quantity')
            add_current_date = today     #reference current date added 
            query = "INSERT INTO shoppinglist (id, itemdescription, quantity,dateadded) VALUES (%s, '%s', %s, %s)" % (add_id, add_item_description, add_quantity, add_current_date)
            execute_query(conn, query)    
    
        elif option == 'd':
            item_to_delete = input('Enter item to delete')
            delete_statement = "DELETE FROM shoppinglist WHERE id = %s" % (item_to_delete)   
            execute_query(conn, delete_statement)
 
        elif option == 'u':
            updated_item_description = input('Enter item to update') #update here
            update_shopping_list = """
            UPDATE shoppinglist
            SET amount = %s
            WHERE id = %s """ % (updated_item_description) 
            execute_query(conn, update_shopping_list)

        elif option == 'r1':    #https://www.w3schools.com/python/python_mysql_orderby.asp to help with the sorting alphhabeitcally for r1 and r2
            sql_item = "SELECT * FROM shoppinglist ORDER BY itemdescription"
            execute_query(conn,sql_item)    
    
        elif option == 'r2':
            sql_quantity = "SELECT * FROM shoppinglist ORDER BY quantity"
            execute_query(conn,sql_quantity)
    
        elif option == 'q':
            pass #to quit

menu()