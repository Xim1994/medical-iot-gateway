from abc import ABC
from typing import List, Dict, Any
from app.infrastructure.bluetooth.ble_connector import BleConnector
import asyncio
from app.domain.device_repository import DeviceRepository

class BleUseCase(ABC):
    def __init__(self, repository: DeviceRepository):
        self.ble_connector = BleConnector()
        self.repository = repository
    
    def scan_and_save_ble_devices(self) -> List[Dict[str, Any]]:
        devices = asyncio.run(self.ble_connector.scan_devices())

        # Save the scanned devices into the SQLite database
        for device in devices:
            self.repository.save(device)

        return devices