from abc import ABC, abstractmethod
from awscrt import mqtt
from typing import Tuple

class IMqttConnector(ABC):
    @abstractmethod
    def connect(self) -> Tuple[mqtt.Connection, str]:
        pass

    @abstractmethod
    def publish_message(self, mqtt_connection: mqtt.Connection, topic: str, message: str) -> str:
        pass

    @abstractmethod
    def disconnect(self, mqtt_connection: mqtt.Connection) -> str:
        pass
