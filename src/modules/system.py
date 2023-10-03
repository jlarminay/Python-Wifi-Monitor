import psutil

def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

def get_ram_usage():
    ram = psutil.virtual_memory()
    return ram.percent

def get_cpu_temperature():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
            temperature = int(file.read()) / 1000.0  # Convert millidegrees to degrees Celsius
            return temperature
    except FileNotFoundError:
        return None  # File not found (not on all Linux systems)