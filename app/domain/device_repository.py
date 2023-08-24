from abc import ABC, abstractmethod
from typing import List
from app.domain.device import Device

class DeviceRepository(ABC):
    @abstractmethod
    def save(self, device: Device) -> None:
        pass

    @abstractmethod
    def get_all(self) -> List[Device]:
        pass
