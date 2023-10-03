import socket

def get_current_ip():
    # Get the current IP address
    try:
        ip = socket.gethostbyname(socket.gethostname())
        return ip
    except socket.gaierror:
        return "Not connected"