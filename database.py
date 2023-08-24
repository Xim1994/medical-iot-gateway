import sqlite3

def create_db_and_table():
    conn = sqlite3.connect('devices.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS devices (
                        id INTEGER PRIMARY KEY,
                        device_name TEXT,
                        device_address TEXT,
                        last_connected_time TEXT)''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db_and_table()
