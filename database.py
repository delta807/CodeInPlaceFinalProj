# Sets up the database and creates 'transactions' table if it doesn't exist.
import sqlite3

DATABASE = 'transactions.db'

def setup_database():
    """Set up the SQLite database and create the transactions table if it doesn't exist."""
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
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
