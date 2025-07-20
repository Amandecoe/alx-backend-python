import sqlite3
import functools

def with_db_connection(func):
    """Decorator to handle database connection"""
    @functools.wraps(func)
    def wrapper(*args, db_name='users.db', **kwargs):
        conn = sqlite3.connect(db_name)
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

def transactional(func):
    """Decorator to handle database transactions"""
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()  # Commit if no exceptions
            return result
        except Exception as e:
            conn.rollback()  # Rollback on error
            raise e  # Re-raise the exception
    return wrapper

@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET email = ? WHERE id = ?", 
        (new_email, user_id)
    )

# Usage
update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
