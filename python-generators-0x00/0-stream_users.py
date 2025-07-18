
import mysql.connector

def stream_users():
  try:
    connection = mysql.connector.connect(  #connect() is a function which creates connection based on properties provided and it belongs to mysql.connector
      host = "localhost",
      user = "root",                 #sets the properties for the connection
      password = "",
      database = "alx_prodev"
    )
    cursor= connection.cursor(dictionary = True)
    cursor.execute("SELECT * FROM user_data")
   
    for row in cursor:
     yield row
  except Exception as b:
    print("Wrong connection")

if __name__ == "__main__":
 for user in stream_users():
   print(user)