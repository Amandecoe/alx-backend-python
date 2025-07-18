import mysql.connector


def stream_users_in_batches(batch_size=5):
  try:
    connection = mysql.connector.connect(  #establishes a connection to a database specified below
      host = "localhost",
      user = "root",                 #sets the properties for the connection
      password = "",
      database = "alx_prodev"
    )
    cursor= connection.cursor(dictionary = True) #the cursor will fetch data from the database in a dictionary format
    offset = 0 #tracks the starting row of each batch
    while True:
      cursor.execute("SELECT * FROM user_data OFFSET %s LIMIT %s", (offset, batch_size))
      batch = cursor.fetchall()   #is a query which fetches all data executed in cursor.execute
      if not batch:   #checks if the batch is empty or not(from the data fetched by cursor.fetchall), if it is empty it returns
        break    #if the batch is empty it stops
      yield batch # if batch is not empty it yields the batch and sends it to the caller
      offset += batch_size  #increases the offset value by the batch size to not repeat the rows fetched before
    cursor.close() #closes the cursor
  except Exception as d:
    print("Wrong connection")

  finally:
    if connection and connection.is_connected():
        cursor.close()
        connection.close()

def batch_processing(batch_size=25):  #processes each batch to filter users over the age of 25
  for batch in stream_users_in_batches():
   filtered_users = [
            user for user in batch 
            if user.get("age", 0) > 25  # Checks age > 25
        ]
   if filtered_users:
     yield filtered_users


if __name__ == "__main__":
  for filtered_users in batch_processing():
        for user in filtered_users:
            print(f"User {user['id']}: {user['name']} (Age: {user['age']})")