# Sets up the database and creates 'transactions' table if it doesn't exist.
import sqlite3

conn = sqlite3.connect('transactions.db')
c = conn.cursor()

def setup_database():
    with conn:
        c.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT,
                expense REAL,
                payor TEXT,
                split TEXT 
            )
        ''')
        conn.commit()
