import sqlite3
import functools
import time
from datetime import datetime


def log_query(func):
    """Simple decorator to log database queries"""
    def wrapper(query):
        print(f"🚀 Running query: {query}")  # Log the query
        
        start_time = time.time()   
        try:          # Start timer
         result = func(query)                 # Run the original function
         end_time = time.time()              # Stop timer
        
         print(f"✅ Done in {end_time-start_time:.2f}s")  # Log time taken
         return result
        except sqlite3.Error as e:
            print(f"❌ Query failed: {e}")
            raise
        finally:
            print("--- Query completed ---\n")
    return wrapper


@log_query
def fetch_all_users(query, params= None):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
print (users)

