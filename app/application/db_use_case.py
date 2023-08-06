from abc import ABC
from typing import Dict, Any, str
from ..domain.interfaces.i_db_connector import IDbConnector

class DbUseCase(ABC):
    def __init__(self, db_connector: IDbConnector):
        self.db_connector = db_connector

    def save_device_to_db(self, device_data: Dict[str, Any]) -> str:
        return self.db_connector.save_device(device_data)