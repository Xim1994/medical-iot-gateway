# app/domain/interfaces/ibleconnector.py

from abc import ABC, abstractmethod
from typing import Any, Dict, List

class IBleConnector(ABC):

    @abstractmethod
    def scan_devices(self) -> List[Dict[str, Any]]:
        pass

