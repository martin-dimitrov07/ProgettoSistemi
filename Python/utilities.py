import socket

def GetIp():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.connect("8.8.8.8", 80) # ip fittizio
    ip = my_socket.getsockname()[0]
    my_socket.close()
    return ip
        