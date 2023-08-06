from abc import ABC
from typing import List, Dict, Any
from ..domain.interfaces.i_api_connector import IApiConnector

class ApiUseCase(ABC):
    def __init__(self, api_connector: IApiConnector):
        self.api_connector = api_connector

    def get_devices_from_api(self) -> List[Dict[str, Any]]:
        return self.api_connector.get_devices()