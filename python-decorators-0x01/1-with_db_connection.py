import sqlite3
import functools

def with_db_connection(func):
    @functools.wraps(func)  # Preserves function metadata
    def wrapper(user_id, db_name='users.db'):
        conn = sqlite3.connect(db_name)
        try:
            return func(conn, user_id)  # Pass connection instead of cursor
        finally:
            conn.close()
    return wrapper

@with_db_connection
def get_user_by_id(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

# Usage
user = get_user_by_id(1)  # Now works with simple user_id
print(user)



##code doesn't work!!!!!