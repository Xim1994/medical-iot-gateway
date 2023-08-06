import unittest
from app.domain.device import Device

class TestDevice(unittest.TestCase):
    def setUp(self):
        self.device = Device(
            endpoint="endpoint",
            cert_filepath="cert_filepath",
            pri_key_filepath="pri_key_filepath",
            ca_filepath="ca_filepath"
        )

    def test_device_initialization(self):
        self.assertEqual(self.device.endpoint, "endpoint")
        self.assertEqual(self.device.cert_filepath, "cert_filepath")
        self.assertEqual(self.device.pri_key_filepath, "pri_key_filepath")
        self.assertEqual(self.device.ca_filepath, "ca_filepath")
