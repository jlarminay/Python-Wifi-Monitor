import socket
import subprocess

def get_current_ip():
    # Get the current IP address
    try:
        # ip = socket.gethostbyname(socket.gethostname())
        # return ip

        # Run the 'hostname -I' command and capture its output
        output = subprocess.check_output(['hostname', '-I'], universal_newlines=True)
        
        # Split the output into a list of IP addresses
        ip_list = output.strip().split()
        
        # Return the first IP address
        if ip_list:
            return ip_list[0]
        else:
            return "Not connected"
    except socket.gaierror:
        return "Not connected"

def is_wifi_connected():
    # Check if the device is connected to Wi-Fi
    try:
        result = subprocess.check_output(["iwgetid"]).decode("utf-8")
        return "ESSID" in result
    except subprocess.CalledProcessError:
        return False