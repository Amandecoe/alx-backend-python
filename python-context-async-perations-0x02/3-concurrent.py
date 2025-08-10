import asyncio
import aiosqlite
import sqlite3

async def _fetch_users(conn): 
 try:
  conn = sqlite3.connect('usersin.db')
  cursor = cursor.conn()
  await cursor.execute('SELECT * USERS from users')
 except sqlite3.Error as d:
  print("Can not connect to database")

async def _fetch_older_users(conn):
 try:
  conn = sqlite3.connect('usersin.db')
  cursor = cursor.conn()
  await cursor.execute ('SELECT USERS WHERE Age > 40')
 except sqlite3.Error as x:
  print ("Can not connect to database")

