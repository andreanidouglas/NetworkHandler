import socket

class UserSocket:
    def __init__(self, ip_in='127.0.0.1', port_in='32001'):
        self._ip = ip_in
        self._port = port_in

    _socket = None
    _buffer = 1024
    _lastReceivedMessage = None
    _out_ip = None
    _out_port = None
    def initialize_socket(self):
        self._socket = socket.socket(socket.AF_INET, # Internet
                            socket.SOCK_DGRAM) # UDP
    def set_ip(self, ip_in):
        self._ip = ip_in
    def get_ip(self):
        return self._ip
    def set_port(self, port_in):
        self._port = port_in
    def get_port(self):
        return self._port
    def get_last_received_message(self):
        return self._lastReceivedMessage
    def get_out_ip(self):
        return self._out_ip
    def get_out_port(self):
        return self._out_port


    def is_initialized(self):
        if (self._socket):
            return True
        else:
            return False
    def send_message(self, message):
        self._socket.sendto(bytes(message, 'UTF-8'), (self._ip, self._port))
    def receive_message(self):
        message_struct = self._socket.recvfrom(self._buffer)
        self._out_ip = message_struct[1][0]
        self._out_port = message_struct[1][1]
        #self._lastReceivedMessage = 
        return message_struct

class Client(UserSocket):
    def __init__(self, client_name):
        self.client_name = client_name


class Server(UserSocket):
    def __init__(self, server_name):
        self.server_name = server_name
