import subprocess

def is_wifi_connected():
    # Check if the device is connected to Wi-Fi
    try:
        result = subprocess.check_output(["iwgetid"]).decode("utf-8")
        return "ESSID" in result
    except subprocess.CalledProcessError:
        return False