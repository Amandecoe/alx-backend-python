import sqlite3



class Database:
 def __init__(conn, users):
  conn = sqlite3.connect("users.db") #connects to a database, creates one if it doesnt exist
  conn.cursor = conn.cursor() #creates a cursor object which is used to access the data in the database


 def create_table(conn):
   try: 
    conn.cursor.execute('''
      CREATE TABLE IF NOT EXISTS users( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          email TEXT UNIQUE NOT NULL,
          age INTEGER) 
     ''')
    conn.commit() #save the changes
    print("Table created successfuly")
  
   except sqlite3.Error as e:
    print ("Table not created: ")
  
 def table_population(conn, name, email, age):
   try:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email, age) VALUES (?,?,?)",(name, email, age))
    conn.commit()
    print("data added succesfully")
   except sqlite3.Error as b:
    print ("Can not add to table")

def main():
 db = Database("users")
 db.create_table()
 db.table_population("Amanuel","runaway21@gmail.com",22)

main()

 


