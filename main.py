from dotenv import load_dotenv
from app.domain.device import Device
from app.application.mqtt_use_cases import MqttUseCase
from app.application.ble_use_case import BleUseCase
from app.infrastructure.database.sqlite_connector import SqliteConnector
import os

load_dotenv()

def main():
    device = Device(
        endpoint=os.getenv("AWS_ENDPOINT"),
        cert_filepath=os.getenv("CERT_FILEPATH"),
        pri_key_filepath=os.getenv("PRIVATE_KEY_FILEPATH"),
        ca_filepath=os.getenv("CA_FILEPATH")
    )

    mqtt_use_case = MqttUseCase(device)
    device_repository = SqliteConnector(db_path="devices.db")
    ble_use_case = BleUseCase(repository=device_repository)

    devices = ble_use_case.scan_ble_devices()

    for device in devices:
        print(device)

    mqtt_connection, message = mqtt_use_case.connect_device()
    if mqtt_connection is None:
        print(f"Error connecting to the device: {message}")
        return
    print(message)

    message = mqtt_use_case.publish_message(mqtt_connection, "$aws/things/Gateway/shadow/update/documents", "Hello world!")
    print(message)

    message = mqtt_use_case.disconnect_device(mqtt_connection)
    print(message)

if __name__ == "__main__":
    main()
