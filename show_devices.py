import sqlite3

def fetch_devices():
    conn = sqlite3.connect('devices.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM devices")
    devices = cursor.fetchall()
    conn.close()
    return devices

if __name__ == "__main__":
    for device in fetch_devices():
        print(device)
