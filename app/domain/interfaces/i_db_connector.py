# app/domain/interfaces/idbconnector.py

from abc import ABC, abstractmethod
from typing import Any, Dict, List
from ..device import Device

class IDbConnector(ABC):

    @abstractmethod
    def save_device(self, device: Device) -> None:
        pass

    @abstractmethod
    def get_devices(self) -> List[Device]:
        pass
