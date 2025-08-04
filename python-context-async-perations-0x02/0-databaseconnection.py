import sqlite3

class DatabaseConnection:
    def __init__(self, db_name='usersin.db'):
        self.db_name = db_name
        self.conn = None
    
    def __enter__(self):
        try:
            self.conn = sqlite3.connect('usersin.db')
            print("Database opened successfully")
            return self.conn
        except sqlite3.Error as e:
            print(f"Cannot open database: {e}")
            raise  # Re-raise to prevent continuation
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            try:
                if exc_type:
                    print(f"Error occurred: {exc_val}")
                    self.conn.rollback()
                else:
                    self.conn.commit()
            except sqlite3.Error as e:
                print(f"Error during commit/rollback: {e}")
                raise
            finally:
                self.conn.close()
                print("Database closed successfully")

# Usage
if __name__ == "__main__":
    try:
        with DatabaseConnection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users')
            result = cursor.fetchall()
            print("Query executed successfully")
            # Process results here
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

     