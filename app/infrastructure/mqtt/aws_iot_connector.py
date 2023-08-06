from app.domain.interfaces.i_mqtt_connector import IMqttConnector
from awscrt import io, mqtt
from awsiot import mqtt_connection_builder
from app.domain.device import Device
import time
from typing import Tuple

class AwsIotConnector(IMqttConnector):
    def __init__(self, device: Device):
        self.device = device
        self.event_loop_group = io.EventLoopGroup(1)
        self.host_resolver = io.DefaultHostResolver(self.event_loop_group)
        self.client_bootstrap = io.ClientBootstrap(self.event_loop_group, self.host_resolver)

    def on_connection_interrupted(self) -> str:
        return "Connection interrupted"

    def on_connection_resumed(self) -> str:
        return "Connection resumed"

    def connect(self) -> Tuple[mqtt.Connection, str]:
        try:
            mqtt_connection = mqtt_connection_builder.mtls_from_path(
                endpoint=self.device.endpoint,
                cert_filepath=self.device.cert_filepath,
                pri_key_filepath=self.device.pri_key_filepath,
                ca_filepath=self.device.ca_filepath,
                client_bootstrap=self.client_bootstrap,
                on_connection_interrupted=self.on_connection_interrupted,
                on_connection_resumed=self.on_connection_resumed,
                client_id="test-" + str(time.time()),
                clean_session=False,
                keep_alive_secs=6
            )
            connect_future = mqtt_connection.connect()
            connect_future.result()
            return mqtt_connection, "Connected!"
        except Exception as e:
                return None, str(e)

    def publish_message(self, mqtt_connection: mqtt.Connection, topic: str, message: str) -> str:
        try:
            mqtt_connection.publish(
                topic=topic,
                payload=message,
                qos=mqtt.QoS.AT_LEAST_ONCE
            )
            return "Message published"
        except Exception as e:
            return str(e)

    def disconnect(self, mqtt_connection: mqtt.Connection) -> str:
        try:
            disconnect_future = mqtt_connection.disconnect()
            disconnect_future.result()
            return "Disconnected"
        except Exception as e:
            return str(e)
