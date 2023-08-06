from bleak import BleakScanner
from app.domain.interfaces.i_ble_connector import IBleConnector
from typing import Any, Dict, List

class BleConnector(IBleConnector):
    
    def __init__(self):
        self.scanner = BleakScanner()

    async def scan_devices(self) -> List[Dict[str, Any]]:
        devices = await self.scanner.discover()
        return [{"address": device.address, "name": device.name} for device in devices]
