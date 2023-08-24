class Device:
    def __init__(self, endpoint, cert_filepath, pri_key_filepath, ca_filepath, name=None, address=None):
        self.name = name
        self.address = address
        self.endpoint = endpoint
        self.cert_filepath = cert_filepath
        self.pri_key_filepath = pri_key_filepath
        self.ca_filepath = ca_filepath
