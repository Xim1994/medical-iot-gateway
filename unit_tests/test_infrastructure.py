import unittest
from unittest.mock import MagicMock, patch
from app.infrastructure.mqtt.aws_iot_connector import AwsIotConnector
from app.domain.device import Device

class TestAwsIotConnector(unittest.TestCase):
    def setUp(self):
        self.device = Device(
            endpoint="endpoint",
            cert_filepath="cert_filepath",
            pri_key_filepath="pri_key_filepath",
            ca_filepath="ca_filepath"
        )
        self.connector = AwsIotConnector(self.device)

    def test_connect(self):
        with patch("app.infrastructure.mqtt.aws_iot_connector.mqtt_connection_builder.mtls_from_path") as mocked_mtls:
            self.connector.connect()
            mocked_mtls.assert_called_once()
