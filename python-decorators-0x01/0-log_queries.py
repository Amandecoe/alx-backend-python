import sqlite3
import time

def log_queries(func):
  def wrapper(*args , **kwargs):
      start = time.time()
      result = func(*args, **kwargs)  # Run the actual query
      duration = time.time() - start
        
        # Get the SQL query (assuming it's the first argument)
      sql = args[0] if args else "No query captured"
      print(f"Query took {duration:.4f} seconds: {sql[:50]}...")  # Show first 50 chars
        
      return result
  return wrapper  

def populate_table(conn, name, email, age):
   conn = sqlite3.connect('usersin.db')
   cursor = conn.cursor()
   try:
      cursor.execute(
         'INSERT INTO TABLE user(name, email, age)'
         'VALUES(?,?,?)', (name, email, age)
      )
      conn.commit()
      print ("data added successfully")
   except sqlite3.Error as k:
      print ("Can not enter data into table")
   finally:
      conn.close()   

def create_table():
   conn = sqlite3.connect('usersin.db')
   cursor = conn.cursor()
   try:
     cursor.execute('''CREATE TABLE IF NOT EXISTS user(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    age INTEGER)''')
     print("Table created successfuly")
     conn.commit()
   except sqlite3.Error as b:
     print("Can not create table")
   finally:
      conn.close()


@log_queries
def fetch_user_data(query):
  conn = sqlite3.connect('usersin.db')
  cursor = conn.cursor()
  cursor.execute(query)
  results = cursor.fetchall()
  conn.close()
  return results


def main():
   conn = sqlite3.connect('usersin.db')
   create_table()
   populate_table(conn,"Aman", "aman123@gmail.com",20)
if __name__ == "__main__":
    main()   

