import mysql.connector
from mysql.connector import Error
import datetime
from datetime import date 




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
 
cursor = conn.cursor(dictionary=True) #to format it as a dictionary 
sql = "SELECT * FROM shoppinglist"   # this is to fetch the table created from sql workbench 
cursor.execute(sql)
rows = cursor.fetchall() #will later use this(rows) in the function when printing out what has been executred to the databse

#create the menu
def menu():
    print('a - Add item')
    print('d - Remove item')
    print('u - Update item details')
    print('r1 - Output all items in alphabetical order')
    print('r2- Output all items by sorted by quantity (ascending)')
    print('q - Quit') 
    option = input('Enter your option')
    while True: #to loop until the 'q' (quit) command is given
      
        if option == 'a':
            add_id = input('Enter id')
            add_item_description = input('Enter item description')
            add_quantity =  input('Enter item quantity')
            add_current_date = date.today()     #reference current date added  used to find the current date   when adding item in the menu #https://stackabuse.com/how-to-format-dates-in-python/  Source used 
            query = "INSERT INTO shoppinglist (id, itemdescription, quantity,dateadded) VALUES (%s, '%s', %s, %s)" % (add_id, add_item_description, add_quantity, add_current_date)
            execute_query(conn, query)    
            print(rows) #to print out the dictionary after the changes have been executed.
            
       
        elif option == 'd':
            item_to_delete = input('Enter item to delete')
            delete_statement = "DELETE FROM shoppinglist WHERE id = %s" % (item_to_delete)  #delete item chosen  
            execute_query(conn, delete_statement)
            print(rows)
        
        elif option == 'u':
            updated_item_description = input('Enter item to update') #update here
            update_shopping_list = """
            UPDATE shoppinglist
            SET amount = %s
            WHERE id = %s """ % (updated_item_description) 
            execute_query(conn, update_shopping_list)
            print(rows)
        
        elif option == 'r1':    #https://www.w3schools.com/python/python_mysql_orderby.asp  Source used to help with the sorting alphhabeitcally for r1 and r2 
            sql_item = "SELECT * FROM shoppinglist ORDER BY itemdescription"
            execute_query(conn,sql_item)    
            print(rows)    
        
        elif option == 'r2':
            sql_quantity = "SELECT * FROM shoppinglist ORDER BY quantity"   #sort by quantity ascending
            execute_query(conn,sql_quantity)
            print(rows)    
        
        elif option == 'q':
            break #to quit

menu()  #to output the menu







