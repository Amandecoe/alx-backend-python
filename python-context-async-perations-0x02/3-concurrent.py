import asyncio
import aiosqlite
import sqlite3

def async_fetch_users(conn): 
 try:
  conn = sqlite3.connect('usersin.db')
  cursor = cursor.conn()
  await cursor.execute('SELECT * USERS from users')
 except sqlite3.Error as d:
  print("Can not connect to database")

def async_fetch_older_users(conn):
 try:
  conn = sqlite3.connect('usersin.db')
  cursor = cursor.conn()
  await cursor.execute ('SELECT USERS WHERE Age > 40')
 except sqlite3.Error as x:
  print ("Can not connect to database")


if __name__ == '__main__':
 asyncio.gather(_fetch_older_users(), _fetch_users())
 asyncio.run(fetch_concurrently())