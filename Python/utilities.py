import socket
import sender
import threading
import costants

def GetIp():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_socket.connect(("8.8.8.8", 80)) # ip fittizio
    ip = my_socket.getsockname()[0]
    my_socket.close()
    return ip
    