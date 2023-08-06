# app/domain/interfaces/iapiconnector.py

from abc import ABC, abstractmethod
from typing import Any, Dict, List

class IApiConnector(ABC):

    @abstractmethod
    def get_devices(self) -> List[Dict[str, Any]]:
        pass
