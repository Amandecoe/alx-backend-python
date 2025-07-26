import sqlite3
import time
import functools


def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = None
        try:
            conn = sqlite3.connect('usersin.db')
            print("Database connection established")
            result = func(conn, *args, **kwargs)
            return result
        except sqlite3.Error as e:
            print("Cannot establish database connection:", e)
            return None
        finally:
            if conn:
                conn.close()
                print("Database closed successfully")
    return wrapper

def retry_on_failure(retires=3 , delay=1):
  def decorator(func):
    @functools.wraps(func)
    def wrapper (conn, *args, **kwargs):
     while True:
       try:

         result = func(conn, *args, **kwargs)
       except sqlite3.error as d:
            
        return wrapper



@with_db_connection


def fetch_users_with_retry(conn):
 cursor = conn.cursor()
 cursor.execute("SELECT * FROM users")
 return cursor.fetchall()