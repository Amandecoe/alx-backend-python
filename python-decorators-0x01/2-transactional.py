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


def transactional(func):
    def wrapper():

     return wrapper    
 
 

@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
 cursor = conn.connect()
 cursor = conn.cursor() 
 cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
#### Update user's email with automatic transaction handling 


def main():
 update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')

if __name__=="__main__":
    main() 