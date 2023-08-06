import unittest
from app.application.mqtt_use_cases import MqttUseCase
from app.domain.device import Device
import os
from dotenv import load_dotenv

load_dotenv()

class TestIntegrationMQTT(unittest.TestCase):

    def setUp(self):
        self.device = Device(
        endpoint=os.getenv("AWS_ENDPOINT"),
        cert_filepath=os.getenv("CERT_FILEPATH"),
        pri_key_filepath=os.getenv("PRIVATE_KEY_FILEPATH"),
        ca_filepath=os.getenv("CA_FILEPATH")
    )
        self.use_cases = MqttUseCase(self.device)

    def test_mqtt_integration(self):
        # Intenta establecer una conexión con el servidor MQTT
        connection, message = self.use_cases.connect_device()
        self.assertIsNotNone(connection, "Failed to connect to MQTT server")

        # Intenta publicar un mensaje en el servidor MQTT
        message = self.use_cases.publish_message(connection, "test/topic", "Hello, world!")
        self.assertEqual(message, "Message published", "Failed to publish message")

        # Intenta desconectar del servidor MQTT
        message = self.use_cases.disconnect_device(connection)
        self.assertEqual(message, "Disconnected", "Failed to disconnect from MQTT server")
