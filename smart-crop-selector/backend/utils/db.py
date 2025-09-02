import sqlite3
import os

def get_db_connection():
    db_path = os.path.join(os.path.dirname(__file__), '../../database/crops.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def save_user_input(data):
    try:
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS user_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            soil_type TEXT,
            rainfall_level TEXT,
            region TEXT,
            crops TEXT
        )''')
        c.execute('INSERT INTO user_history (soil_type, rainfall_level, region, crops) VALUES (?, ?, ?, ?)',
                  (data['soil_type'], data['rainfall_level'], data['region'], ','.join(data.get('crops', []))))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print('DB Error:', e)
        return False

def get_user_history():
    try:
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM user_history ORDER BY id DESC LIMIT 10')
        rows = c.fetchall()
        conn.close()
        return [dict(row) for row in rows]
    except Exception as e:
        print('DB Error:', e)
        return []
