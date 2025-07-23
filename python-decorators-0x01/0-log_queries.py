import sqlite3

def log_queries(func):
  def wrapper():
    



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
   except sqlite3.Error as b:
     print("Can not create table")


def fetch_user_data(query):
  conn = sqlite3.connect('usersin.db')
  cursor = conn.cursor()
  cursor.execute()
  results = cursor.fetchall()
  conn.close()
  return results



users = fetch_user_data(query = "SELECT * FROM users")