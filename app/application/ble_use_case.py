from abc import ABC
from typing import List, Dict, Any
from app.infrastructure.bluetooth.ble_connector import BleConnector
import asyncio

class BleUseCase(ABC):
    def __init__(self):
        self.ble_connector = BleConnector()

    def scan_ble_devices(self) -> List[Dict[str, Any]]:
        return asyncio.run(self.ble_connector.scan_devices())