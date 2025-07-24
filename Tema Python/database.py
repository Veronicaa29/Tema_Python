import sqlite3
from datetime import datetime

DB_FILE = "operations.db"


def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY,
            operation TEXT,
            input TEXT,
            result TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()


def save_request(operation: str, input_data: str, result: str):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        INSERT INTO requests (operation, input, result, timestamp)
        VALUES (?, ?, ?, ?)
    ''', (operation, input_data, result, datetime.now().isoformat()))
    conn.commit()
    conn.close()
