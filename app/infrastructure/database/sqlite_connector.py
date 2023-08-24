import sqlite3
from app.domain.device_repository import DeviceRepository
from app.domain.device import Device
from typing import List

class SqliteConnector(DeviceRepository):
    def __init__(self, db_path: str):
        self._db_path = db_path

    def save(self, device: Device) -> None:
        with sqlite3.connect(self._db_path) as conn:
            cursor = conn.cursor()
            
            # Check if device with the same address already exists
            cursor.execute("SELECT COUNT(*) FROM devices WHERE device_address = ?", 
                        (device.get('address', None),))
            if cursor.fetchone()[0] == 0:
                # If not found, insert the new device
                cursor.execute("INSERT INTO devices (device_name, device_address) VALUES (?, ?)", 
                            (device.get('name', None), device.get('address', None)))
                conn.commit()


    def get_all(self) -> List[Device]:
        with sqlite3.connect(self._db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT device_name, device_address FROM devices")
            rows = cursor.fetchall()

        return [Device(name=row[0], address=row[1]) for row in rows]
