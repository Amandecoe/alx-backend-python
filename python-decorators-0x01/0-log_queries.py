import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(f"{db_name}.db")  # Added .db extension
        self.cursor = self.conn.cursor()  # Fixed cursor creation

    def create_table(self):
        try: 
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS users( 
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    age INTEGER) 
            ''')
            self.conn.commit()
            print("Table created successfully")
        except sqlite3.Error as e:
            print(f"Table not created: {e}")  # Added error message

    def table_population(self, name, email, age):
        try:
            self.cursor.execute(
                "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
                (name, email, age)
            )
            self.conn.commit()
            print("Data added successfully")
        except sqlite3.Error as e:
            print(f"Cannot add to table: {e}")  # Added error message
    def retrieve_data(self):
        try:
            self.cursor.execute(
            "SELECT * FROM users"
           )
            rows = self.cursor.fetchall()
            if not rows:
                print("no data found in table")
                return []
        
            print("data retrieved successfully")
            for row in rows:
                print(row)
                return rows  
            
        except sqlite3.Error as J:
            print("Can not retrieve data")
            
def main():
    db = Database("db_name")  # Will create users.db
    db.retrieve_data()
    db.conn.close()  # Important to close connection

if __name__ == "__main__":
    main()

 


