import sqlite3
import functools

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = None
        try:
            conn = sqlite3.connect('usersin.db')
            print("Database connection established")
            result = func(conn, *args, **kwargs)
            conn.commit()
            return result
        except sqlite3.Error as e:
            print("Cannot establish database connection:", e)
            return None
        finally:
            if conn:
                conn.close()
                print("Database closed successfully")
    return wrapper

@with_db_connection
def get_user_by_id(conn, age):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE age = ?", (age,))
        user = cursor.fetchone()
        if user is None:
            print(f"No user found with age {age}")
        else:
            print(f"User found: {user}")
        return user
    except sqlite3.Error as e:
        print(f"Query execution error: {e}")
        return None


def main():
    user = get_user_by_id(20)  # Only pass age, decorator handles connection
    print(user)

if __name__ == "__main__":
    main()

