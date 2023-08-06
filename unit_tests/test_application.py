import unittest
from unittest.mock import MagicMock
from app.application.mqtt_use_cases import MqttUseCase
from app.domain.device import Device

class TestUseCases(unittest.TestCase):
    def setUp(self):
        self.device = Device(
            endpoint="endpoint",
            cert_filepath="cert_filepath",
            pri_key_filepath="pri_key_filepath",
            ca_filepath="ca_filepath"
        )
        self.use_cases = MqttUseCase(self.device)

    def test_connect_device(self):
        self.use_cases.connector.connect = MagicMock(return_value=("connection", "Connected!"))
        connection, message = self.use_cases.connect_device()
        self.assertEqual(connection, "connection")
        self.assertEqual(message, "Connected!")
