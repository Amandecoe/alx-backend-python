import asyncio
import aiosqlite
import sqlite3

async def _fetch_users(): 
 conn = sqlite3.connect('userindb')
 cursor = cursor.conn()
 cursor.execute('SELECT * USERS from users')


async def 