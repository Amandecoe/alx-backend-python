import sqlite3
import functools

def with_db_connection(func):
    def wrapper(*args, **kwargs):
     try:
         conn = sqlite3.connect('usersin.db')
         cursor = conn.cursor()
         print("Databse connection established")
         result = func( *args , **kwargs)
         conn.commit()
         return result
     except sqlite3.Error as b:
          print("Can not establish database connection")
     finally:
          conn.close()  
    return wrapper    

@with_db_connection
def get_user_by_id(conn, age):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE age = ?", (age))
    return cursor.fetchone()


def main():
 conn = sqlite3.connect('usersin.db')
 user = get_user_by_id(conn,20)  # Now works with simple user_id
 print(user)


if __name__=="__main__":
 main()


