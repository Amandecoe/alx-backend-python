import time
import sqlite3 
import functools
from functools import wraps

query_cache = {}

def cache_query(func):
    """Decorator that caches query results based on the SQL query string"""
    @wraps(func)
    def wrapper(conn, query, *args, **kwargs):
        # Create a cache key using the query and parameters
        cache_key = (query, tuple(kwargs.items()))
        
        # Return cached result if available
        if cache_key in query_cache:
            print("Returning cached result for query:", query)
            return query_cache[cache_key]
            
        # Execute and cache if not in cache
        result = func(conn, query, *args, **kwargs)
        query_cache[cache_key] = result
        print("Caching new result for query:", query)
        return result
    return wrapper

# Database connection decorator
def with_db_connection(func):
    @wraps(func)
    def wrapper(*args, db_name='users.db', **kwargs):
        conn = sqlite3.connect(db_name)
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# First call will execute and cache the result
print("First call:")
users = fetch_users_with_cache(query="SELECT * FROM users")

# Second call will use the cached result
print("\nSecond call:")
users_again = fetch_users_with_cache(query="SELECT * FROM users")