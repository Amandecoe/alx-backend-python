
import mysql.connector #imports the mysql connector module to enable database operations

def stream_users():
  try:
    connection = mysql.connector.connect(  #establishes a connection to a database specified below
      host = "localhost",
      user = "root",                 #sets the properties for the connection
      password = "",
      database = "alx_prodev"
    )
    cursor= connection.cursor(dictionary = True)  #cursor is a pointer to a database or points to a database, the use of dictionary here makes each row return as a column:value
    cursor.execute("SELECT * FROM user_data") #is what is used to run an sql query. fetches every row here
   
    for row in cursor:
     yield row     #loops through each row in the query result and instead of returing all at once it yields one row at a time
  except Exception as b:
    print("Wrong connection")

if __name__ == "__main__":
 for user in stream_users():
   print(user)    #iterators over the above generator fetching each row as a dictionary as provided in the function