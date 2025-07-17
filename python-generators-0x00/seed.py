import mysql.connector
from mysql.connector import Error

def connect_db(): #function to connect to mysql server/our mysql server is named connection here
  try:
    connection = mysql.connector.connect(  #connect() is a function which creates connection based on properties provided and it belongs to mysql.connector
      host = "localhost",
      user = "root",                 #sets the properties for the connection
      password = ""
    )
    return connection
  except Exception as e:
    print(f"Error detected connecting to mysql: {e}")  
    return None
  
def create_database(connection):   #creates a database from the mysql connection we set up in connect_db
 try:
  mycursor = connection.cursor()  
  mycursor.execute("Create database IF NOT EXISTS ALX_prodev")#cursor allows python to connect to the mysql server and execute create, insert, select etc
  print("Database 'ALX_prodev' created or already exists")
 except Exception as b:
  print(f"Error creating database: {b}")
 finally:
   mycursor.close()

def connect_to_prodev():
  try:
    connection = mysql.connector.connect(  #connect() is a function which creates connection based on properties provided and it belongs to mysql.connector
      host = "localhost",
      user = "root",                
      password = "",
      database = "ALX_prodev"
    )
    return connection
  except Exception as c:
    print (f"Error connecting to ALX_prodev: {c}")
    return None 
  
def create_table(connection):   #A function to create a table in the mysql connection we are connected to 
  try:
    mycursor= connection.cursor()
    mycursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id VARCHAR(36) PRIMARY KEY AUTO INCREMENT,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL(10, 2) NOT NULL,
                INDEX (user_id)
            )
        """)
    print ("Table 'user_data' created or already exists.")
  except Exception as d:
    print (f"Error creating the table: {d}")
  finally:
        mycursor.close()

if __name__ == "__main__":
    # First connect to MySQL server
    connection = connect_db()
    if connection:
        # Create the database
        create_database(connection)
        connection.close()  # Close the initial connection
        
        # Now connect to the specific database
        prodev_connection = connect_to_prodev()
        if prodev_connection:
            # Create the table
            create_table(prodev_connection)
            prodev_connection.close()        