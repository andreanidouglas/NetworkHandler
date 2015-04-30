import socket

class user_socket:
    _ip='127.0.0.1'
    _port=32001
    _socket=None
    _buffer=1024
    _lastReceivedMessage=None

    _outIp=None
    _outPort=None
    def initialize_socket(self):
       self._socket = socket.socket(socket.AF_INET, # Internet
                            socket.SOCK_DGRAM) # UDP
    def setIp(self, ip):
        self._ip=ip
    def getIp(self):
        return self._ip
    def setPort(self, port):
        self._port=port
    def getPort(self):
        return self._port
    def getLastReceivedMessage(self):
        return self._lastReceivedMessage
    def getOutIp(self):
        return self._outIp
    def getOutPort(self):
        return self._outPort


    def isInitialized(self):
        if (self._socket):
            return True
        else:
            return False
    def sendMessage(self, message):
        self._socket.sendto(bytes(message, 'UTF-8'), (self._ip, self._port))
    def receiveMessage(self):
        message_struct = self._socket.recvfrom(self._buffer)
        self._outIp=message_struct[1][0]
        self._outPort=message_struct[1][1]
        #self._lastReceivedMessage = 
        return message_struct

class client(user_socket):
    def __init__(self, client_name):
        self.client_name=client_name


class server(user_socket):
    def __init__(self, server_name):
        self.server_name=server_name

if __name__ == "__main__":
    new_client = client("cliente 1")
    if not (new_client.isInitialized()):
        new_client.initialize_socket()
    print(new_client.getIp())
    new_client.sendMessage("Ola Mundo")
    new_client.receiveMessage();
    #print(new_client.getLastReceivedMessage())
    print(new_client.getOutIp())
