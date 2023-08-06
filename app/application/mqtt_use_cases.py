from abc import ABC
from ..infrastructure.mqtt.aws_iot_connector import AwsIotConnector
from ..domain.device import Device

class MqttUseCase(ABC):
    def __init__(self, device: Device):
        self.connector = AwsIotConnector(device)

    def connect_device(self):
        return self.connector.connect()

    def publish_message(self, connection, topic, message):
        return self.connector.publish_message(connection, topic, message)

    def disconnect_device(self, connection):
        return self.connector.disconnect(connection)
