# Aquí podríamos definir un dispositivo de AWS IoT Core como entidad de dominio
class Device:
    def __init__(self, endpoint, cert_filepath, pri_key_filepath, ca_filepath):
        self.endpoint = endpoint
        self.cert_filepath = cert_filepath
        self.pri_key_filepath = pri_key_filepath
        self.ca_filepath = ca_filepath
