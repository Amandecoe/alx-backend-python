import sqlite3

class DatabaseConnection:
    def __init__(self, db_name='usersin.db'): #constructor which initializes an object
        self.db_name = db_name
        self.conn = None
    
    def __enter__(self):
        try:
            self.conn = sqlite3.connect('usersin.db')
            print("Database opened successfully")
            return self.conn
        except sqlite3.Error as e:
            print(f"Cannot open database:")
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn: #if this 'conn' exists continue with the following
            try:
                if exc_type: #if there is an exception 
                    print(f"Error occurred: {exc_val}")
                    self.conn.rollback() #rollback the connection again if the error occurs
                else:
                    self.conn.commit() #if there is no error just save it and continue 
            except sqlite3.Error as e:
                print(f"Error during commit/rollback: {e}")
                raise
            finally:
                self.conn.close() #close the conneciton when you are done checking the above 
                print("Database closed successfully")


if __name__ == "__main__":
    try:
        with DatabaseConnection() as conn: #let the class accept any value as a database by leaving the brackets blank
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users')
            result = cursor.fetchall()
            print("Query executed successfully")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

     